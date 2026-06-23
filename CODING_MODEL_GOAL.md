# Coding Model Fine-Tune Goal

## Objective

Build a small but credible learning project that fine-tunes an open-source coding model once, then reports verifiable coding metrics.

The goal is not to train a model from scratch or beat ChatGPT generally. The goal is to copy the high-ROI idea from the transcript:

> Pick one narrow coding format, train a capable open model for that format, and evaluate with executable tests.

## Target Claim

Aim for a result like:

```text
I fine-tuned Qwen2.5-Coder-7B-Instruct on Python bug-fix diff tasks.
On a held-out executable eval set, my fine-tuned model improved over the base model
and compared competitively with older open coding models.
```

Example final table:

| Model | Eval Tasks Passed |
| --- | ---: |
| CodeLlama-7B-Instruct | 18/100 |
| Base Qwen2.5-Coder-7B-Instruct | 31/100 |
| Fine-tuned Qwen2.5-Coder-7B-Instruct | 43/100 |

The actual numbers will come from the evaluation run.

## Scope

Train once. Do not spend weeks iterating.

Use a single, narrow task:

```text
Python bug fix -> unified diff
```

The model receives:

```text
- an instruction
- buggy code
- failing test or expected behavior
```

The model must output:

```text
only a unified diff
```

## Model

Preferred base model:

```text
Qwen2.5-Coder-7B-Instruct
```

Why:

- strong enough to create a real result
- small enough for one rented GPU
- much better wow factor than a 1.5B toy model
- already good at code, so fine-tuning can focus on format and task behavior

Fallback if compute is too tight:

```text
Qwen2.5-Coder-3B-Instruct
```

## Training Method

Primary method:

```text
QLoRA fine-tuning with Unsloth
```

Planned training setup:

```text
epochs: 1
train examples: 5,000-10,000
output: LoRA adapter
```

Do not full fine-tune the model. The point is to learn the practical workflow without burning credits.

## DeepSeek-R1-Style RLVR Option

The repo already contains a small GRPO/RLVR demo in `llm_env_demo/`. That is useful because DeepSeek-R1 also used GRPO-style reinforcement learning with rule-based rewards.

For this coding project, do not replace QLoRA SFT with RLVR. Use this order:

```text
1. Cold-start SFT: QLoRA on validated bug-fix diff examples
2. Optional RLVR: GRPO on a smaller set of executable coding tasks
```

Why:

- SFT teaches the model the desired diff format cheaply and reliably.
- RLVR is only useful if the reward is strong, such as tests passing after applying the patch.
- Starting with RLVR directly is risky because the model may produce invalid diffs and waste compute.
- DeepSeek-R1 itself used cold-start data before RL for the stronger R1 pipeline, while R1-Zero showed that pure RL can work but has readability and formatting problems.

If RLVR is included, keep it small (sized for the 4090):

```text
RL method: GRPO
RL examples: 200-300 coding tasks (keep it small on 24GB)
generations per prompt: 2 (NOT 4 — 4 is too tight on a 4090)
reward: format + diff applies + tests pass
epochs/steps: short budget-limited run (~2-3 hours)
```

Code reuse: the existing GRPO/RLVR demo in `llm_env_demo/` provides the training loop
structure. Reuse that scaffolding (GRPO trainer setup, generation loop, logging) and
swap in the coding reward function described below (format + git-apply + tests-pass).
The reward function is the main thing that gets rewritten; the training-loop plumbing is
largely reused. Exact reuse boundary can be finalized when reading `llm_env_demo/`.

Memory handling: SFT and GRPO have different memory profiles. After SFT finishes and you
are happy with the eval, fully unload the SFT setup (delete model/optimizer references,
`torch.cuda.empty_cache()`) before constructing the GRPO trainer, then load the base
model + SFT LoRA adapter as the GRPO starting point.

Suggested coding reward:

```text
+0.2 valid unified diff
+0.2 patch applies cleanly
+0.6 tests pass after patch
```

Use RLVR as a final verification-tuning stage, not as the main training method.

## Dataset

Each training row should look like:

```json
{
  "instruction": "Fix the bug. Return only a unified diff.",
  "input": "buggy file contents plus failing test or expected behavior",
  "output": "correct unified diff"
}
```

Concrete data sources (in priority order):

1. **BugsInPy** — ~300-500 real Python bugs from open-source projects, each with a
   buggy commit, a fix commit, and runnable tests. This is the highest-quality source
   because every example has a real executable test harness. Reserve a held-out slice
   of BugsInPy instances for evaluation (never train on those — see Evaluation).
2. **Synthetic bug/fix pairs** — take clean, working Python files and have an LLM inject
   a realistic bug (off-by-one, wrong operator, bad boundary condition, etc.). The
   original file is the "fixed" version; the corrupted file is the "buggy" input. Generate
   the unified diff with Python's `difflib` (`difflib.unified_diff`) between buggy and
   fixed. This is how you scale from a few hundred real bugs to 5k-10k examples cheaply.
3. **SWE-bench train split** — pull the training-eligible instances (SWE-bench Lite has
   ~300 instances with real test harnesses) and convert them to the diff format below.
   These are real GitHub issue fixes and add diversity. NOTE: this is using SWE-bench
   *data for training* — it is separate from *running SWE-bench as a benchmark* (see
   Public Benchmarks). LiveCodeBench problems are standalone coding (not bug-fix diffs),
   so they are less useful as training data; only adapt a subset if convenient.

Target mix: real bugs (BugsInPy train slice + SWE-bench train) for grounding, padded out
to 5k-10k total with synthetic pairs.

Quality bar (apply as an automated filter before training):

- diff must apply cleanly (verify with `git apply --check`)
- fixed code must pass tests when tests are available
- no eval examples in training data (hard split — see Evaluation)
- remove trivial / no-op / comment-only / whitespace-only changes
- reject malformed or empty diffs
- cap diff size (drop huge multi-file diffs that don't fit the narrow task)

## Evaluation

Main evaluation:

```text
100 held-out Python bug-fix tasks
```

Eval set source (must NOT overlap training data):

- Held-out BugsInPy instances that were never included in training.
- Plus hand-curated bug-fix examples from small repos, if more are needed to reach 100.
- This is a deliberate held-out set from a separate slice, NOT a random split of the
  training data. Lock the eval instance IDs before training so there is no leakage.

Executable eval harness (per task):

```text
1. Create an isolated working dir with tempfile.mkdtemp()
2. Clone the repo at the buggy commit (or copy the buggy file in)
3. Write the model's output to a .patch file
4. Run `git apply --check patchfile`  -> records diff_apply_rate
5. If it passes, run `git apply patchfile` to apply it
6. Run the task's tests with a 60-second timeout  -> records test_pass_rate
7. Clean up the temp dir (always, even on failure)
```

Inference settings for eval (use identical settings for every model compared):

```text
loading: transformers + peft, 4-bit
batch size: 1
temperature: 0.0 (greedy, deterministic)
max_new_tokens: 1024
```

Metrics:

```text
diff_apply_rate = percentage of model diffs that apply cleanly
test_pass_rate = percentage of tasks where patched code passes tests
format_success_rate = percentage of outputs that are valid unified diffs
```

Primary score:

```text
test_pass_rate
```

Compare against:

```text
- base Qwen2.5-Coder-7B-Instruct
- fine-tuned Qwen2.5-Coder-7B-Instruct
- optionally CodeLlama-7B-Instruct or another older coding model
```

Avoid relying only on public benchmarks because contamination is easy. The transcript specifically showed that benchmark contamination can make a result look better than it is.

## Public Benchmarks

Also run popular public coding benchmarks as secondary comparisons. These are not the main success metric, but they make the project easier to compare with known models.

IMPORTANT sequencing: these are committed deliverables but run them as STRETCH GOALS,
only AFTER the private 100-task eval confirms the fine-tuned model beats the base model.
Running these benchmarks (especially SWE-bench, which spins up a Docker container per
instance and installs repo dependencies) can take hours of infra setup. Do not invest
that time benchmarking a model that hasn't first proven itself on the cheap private eval.

Priority benchmarks:

```text
1. Aider Polyglot
2. SWE-bench Lite or SWE-bench Verified
3. LiveCodeBench
```

Why these:

- `Aider Polyglot` is the benchmark discussed in the transcript and is relevant to code-edit/diff behavior.
- `SWE-bench` is closer to real GitHub issue fixing and tests whether the model can make practical code changes.
- `LiveCodeBench` measures coding problem-solving on newer problems and is useful for checking broader coding ability.

Expected benchmark plan:

| Benchmark | Purpose | Priority |
| --- | --- | --- |
| Aider Polyglot | Compare directly to the transcript-style coding edit benchmark | High |
| SWE-bench Lite/Verified | Measure real issue-fixing ability | High |
| LiveCodeBench | Measure broader coding problem-solving on newer tasks | Medium |

Also collect public reference scores where available for:

```text
- base Qwen2.5-Coder-7B-Instruct
- CodeLlama-7B-Instruct
- CodeLlama-13B-Instruct
- DeepSeek-Coder 6.7B
- GPT-3.5-style older closed model result, if an official/comparable score exists
```

Optional arena-style comparison:

```text
If there is no practical way to submit the model to a live arena, create a small local arena instead:

- sample 50 coding prompts
- generate answers from base model and fine-tuned model
- hide model names
- judge with executable tests when possible
- optionally use an LLM judge only for non-executable cases
```

Report public benchmarks separately from the held-out private eval:

```text
Private executable eval: main metric
Public benchmarks: comparison/context
Arena-style eval: qualitative side-by-side demo
```

## Compute Budget

Primary target hardware:

```text
1x NVIDIA RTX 4090 (24GB) on a personal server
```

This is the machine the project will actually run on. The plan below is sized for a
single 4090. Cloud GPUs (Brev credits, A100/L40S/etc.) are only a fallback if the
4090 is unavailable.

4090 feasibility notes:

- Qwen2.5-Coder-7B-Instruct QLoRA (4-bit) fits comfortably in 24GB.
- If memory is tight during GRPO, fall back to Qwen2.5-Coder-3B-Instruct.
- GRPO is the tight part on 24GB: keep `num_generations` at 2 (not 4) and 200-300 tasks.
- SFT and GRPO have different memory profiles. Fully unload the SFT training setup
  (free the model + optimizer, empty CUDA cache) before loading the GRPO setup.

Expected runtime on the 4090:

```text
QLoRA SFT (1 epoch, 5k-10k examples): 4-8 hours
GRPO/RLVR pass (200-300 tasks, num_generations=2): 2-3 hours
```

Fallback cloud GPUs (only if no 4090 access):

```text
A100 40GB: fastest
L40S / A10 / L4: slower, see original estimates
$60 Brev credits available
```

Important:

- prepare and validate all data locally before touching the GPU
- run a tiny smoke test (10-20 examples, a few steps) before the full fine-tune
- if using a rented cloud instance, stop it immediately when training/eval is done

## Environment

Target machine: personal server with 1x RTX 4090, CUDA 12.x.

Core stack (pin exact versions in a `requirements.txt` at install time — versions below
are the libraries to pin, not final numbers; resolve compatible versions when you set up):

```text
unsloth          # QLoRA fine-tuning + fast kernels
transformers     # model loading / generation
peft             # LoRA adapters
trl              # GRPO trainer for the RLVR stage
datasets         # data loading / processing
bitsandbytes     # 4-bit quantization
accelerate       # device/training plumbing
torch            # CUDA 12.x build
```

Setup notes:

- Create a fresh virtualenv / conda env on the server after cloning.
- Install a torch build matching the server's CUDA 12.x.
- Run the smoke test (10-20 examples, a few steps) to confirm the env works before the
  full run.
- Data prep can be done on the Mac; training/eval happens on the 4090 server.

## Execution Sequence

Build the project in this order. Steps 5-7 are "run only if the earlier steps look good"
— sequenced so no time is wasted benchmarking a broken model.

```text
1. Data prep        — BugsInPy + synthetic (difflib) + SWE-bench train split,
                      apply quality filters, lock held-out eval IDs (do on Mac)
2. QLoRA SFT        — 1 epoch, 5k-10k examples, output LoRA adapter (4090)
3. Private eval     — 100 held-out tasks, executable harness, vs base model
                      (gate: fine-tuned must beat base before continuing)
4. GRPO/RLVR pass   — 200-300 tasks, num_generations=2, then re-eval
5. Aider Polyglot   — stretch / run if eval looks good
6. SWE-bench Lite   — stretch / run if eval looks good
7. LiveCodeBench    — stretch / run if eval looks good
   (+ optional CodeLlama-7B comparison inference, last, if time allows)
```

The hard gate is step 3: if the fine-tuned model does not beat the base model on the
private eval, fix SFT/data before spending time on GRPO or public benchmarks.

## Deliverables

Final project should produce:

```text
1. requirements.txt with pinned versions
2. data prep scripts (BugsInPy loader, synthetic generator, SWE-bench converter, filters)
3. training data file(s) + locked held-out eval set with instance IDs
4. LoRA adapter
5. training config (SFT and, if run, GRPO)
6. eval script + executable harness (clone/apply/test/cleanup)
7. results table (private eval, with diff_apply / test_pass / format_success rates)
8. optional RLVR reward curve if the GRPO stage is run
9. optional public benchmark results (Aider Polyglot, SWE-bench, LiveCodeBench)
10. short writeup explaining method, data, compute, and limitations
```

## Success Criteria

Minimum success:

```text
Fine-tuned model beats the base model on held-out test_pass_rate.
```

Good success:

```text
Fine-tuned model beats the base model by at least 5 percentage points.
```

Wow-factor success:

```text
Fine-tuned 7B model beats an older open coding model on the same executable eval.
```

## Non-Goals

Do not:

- train from scratch
- chase general ChatGPT quality
- run many expensive iterations
- use contaminated benchmark data
- optimize for loss only
- report unverifiable vibes as results

## One-Sentence Version

Fine-tune `Qwen2.5-Coder-7B-Instruct` with QLoRA on 5k-10k validated Python bug-fix-to-diff examples, optionally add a small GRPO/RLVR pass using executable rewards, then evaluate it against the base model on held-out coding tasks and public coding benchmarks.
