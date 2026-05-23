# train.py
# GRPO training loop.
# This is where the LLM's weights actually get updated
# based on the judge's scores.

import torch
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
from trl import GRPOConfig, GRPOTrainer
from datasets import Dataset

from problems import get_prompts
from judge import judge

# ── CONFIG ────────────────────────────────────────────────────────────────────

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"  # Small enough to run anywhere
OUTPUT_DIR = "./checkpoints"
NUM_EPOCHS = 3                               # Keep low for quick experiment
NUM_GENERATIONS = 4                          # How many attempts per prompt per step
MAX_NEW_TOKENS = 64                          # Answers are short
LEARNING_RATE = 5e-6

# ── LOAD MODEL ────────────────────────────────────────────────────────────────

print(f"Loading model: {MODEL_NAME}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)
print("Model loaded.")

# ── PREPARE DATASET ───────────────────────────────────────────────────────────

raw_problems = get_prompts()

# GRPO trainer expects a HuggingFace Dataset with a 'prompt' column
# We store the answer in a separate column for the reward function
dataset = Dataset.from_list([
    {"prompt": p["prompt"], "answer": p["answer"], "category": p["category"]}
    for p in raw_problems
])

print(f"Dataset: {len(dataset)} problems")

# ── REWARD FUNCTION ───────────────────────────────────────────────────────────

# Track rewards over time for plotting later
reward_log = []

def reward_function(completions, prompts, **kwargs):
    """
    Called by GRPO trainer after each batch of generations.

    Args:
        completions: list of LLM outputs (strings)
        prompts: the input prompts (used to look up correct answers)

    Returns:
        list of float scores (0.0 or 1.0 per completion)

    How GRPO uses this:
        - Generates NUM_GENERATIONS completions per prompt
        - Scores each with this function
        - Completions that scored higher → their tokens get higher probability
        - Completions that scored lower → their tokens get lower probability
    """
    # Get correct answers from the dataset (match by prompt)
    prompt_to_answer = {p["prompt"]: p["answer"] for p in raw_problems}

    scores = []
    for completion, prompt in zip(completions, prompts):
        correct_answer = prompt_to_answer.get(prompt, "")
        score = judge(completion, correct_answer)
        scores.append(score)

    # Log for plotting
    avg_score = sum(scores) / len(scores) if scores else 0
    reward_log.append(avg_score)
    print(f"  Batch avg reward: {avg_score:.3f} | Scores: {scores}")

    return scores

# ── GRPO CONFIG ───────────────────────────────────────────────────────────────

config = GRPOConfig(
    output_dir=OUTPUT_DIR,
    num_train_epochs=NUM_EPOCHS,
    per_device_train_batch_size=4,
    num_generations=NUM_GENERATIONS,       # Key GRPO param: attempts per prompt
    max_completion_length=MAX_NEW_TOKENS,
    learning_rate=LEARNING_RATE,
    logging_steps=1,
    save_strategy="epoch",
    report_to="none",                      # Disable wandb for simplicity
)

# ── TRAINER ───────────────────────────────────────────────────────────────────

trainer = GRPOTrainer(
    model=model,
    args=config,
    train_dataset=dataset,
    reward_funcs=reward_function,
)

# ── TRAIN ─────────────────────────────────────────────────────────────────────

print("\nStarting GRPO training...")
print("Watch the 'Batch avg reward' — it should trend upward over time.\n")

trainer.train()

print("\nTraining complete!")

# Save reward log for plotting
with open("reward_log.json", "w") as f:
    json.dump(reward_log, f)
print("Reward log saved to reward_log.json")

# Save final model
trainer.save_model(f"{OUTPUT_DIR}/final")
print(f"Model saved to {OUTPUT_DIR}/final")
