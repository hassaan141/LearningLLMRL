# RLVR Training Demo

This is a small reinforcement learning with verifiable rewards demo. We trained a small instruction model to answer short machine learning questions, then scored each answer with a deterministic reward function.

## What We Did

- Loaded `Qwen/Qwen2.5-0.5B-Instruct`.
- Created a small dataset of exact-answer ML questions in `problems.py`.
- Used GRPO training from `trl` in `train.py`.
- Generated multiple completions per prompt.
- Scored each completion with `judge.py`.
- Saved the final trained model to `checkpoints/final`.
- Logged batch rewards to `reward_log.json`.
- Plotted the training reward curve with `plot.py`.

## Reward Curve

![RLVR reward curve](reward_curve.png)

## What We Found

The reward generally stayed above the random baseline and reached many perfect-reward batches near the end of training. This suggests the model learned to produce answers that satisfy the verifier for this small task.

The result is a good proof of concept: the training loop, reward logging, model checkpointing, and plotting all worked.

## Important Caveat

The reward function is intentionally simple. It gives full credit when the expected answer appears anywhere in the model output. That makes it useful for a toy RLVR demo, but it can over-credit answers that merely mention the right word.

For a stronger experiment, the next step would be to add held-out evaluation questions and make the judge stricter about exact answers, especially for numeric answers like `0` and `1`.

## How To Reproduce

```bash
source venv/bin/activate
python train.py
python plot.py
python evaluate.py
```
