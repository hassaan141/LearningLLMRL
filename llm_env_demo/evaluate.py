# evaluate.py
# Compare base model vs trained model on all problems.

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from problems import get_prompts
from judge import judge

def evaluate_model(model, tokenizer, problems, label="Model"):
    scores = []
    print(f"\n{'='*50}")
    print(f"Evaluating: {label}")
    print('='*50)

    for p in problems:
        inputs = tokenizer(p["prompt"], return_tensors="pt").to(model.device)

        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=64,
                do_sample=False,           # Greedy for evaluation
                temperature=1.0,
                pad_token_id=tokenizer.eos_token_id
            )

        # Decode only the new tokens (not the prompt)
        new_tokens = output[0][inputs['input_ids'].shape[1]:]
        response = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()

        score = judge(response, p["answer"])
        scores.append(score)

        status = "✓" if score == 1.0 else "✗"
        print(f"{status} [{p['category']}] Expected: '{p['answer']}' | Got: '{response[:40]}'")

    accuracy = sum(scores) / len(scores)
    print(f"\nAccuracy: {accuracy:.1%} ({int(sum(scores))}/{len(problems)})")
    return accuracy


MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
TRAINED_PATH = "./checkpoints/final"

problems = get_prompts()
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Base model
print("Loading base model...")
base_model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)
base_acc = evaluate_model(base_model, tokenizer, problems, "Base Model (untrained)")

# Trained model
print("\nLoading trained model...")
trained_model = AutoModelForCausalLM.from_pretrained(
    TRAINED_PATH,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)
trained_acc = evaluate_model(trained_model, tokenizer, problems, "RLVR Trained Model")

# Summary
print(f"\n{'='*50}")
print(f"RESULTS SUMMARY")
print(f"{'='*50}")
print(f"Base model accuracy:    {base_acc:.1%}")
print(f"Trained model accuracy: {trained_acc:.1%}")
print(f"Improvement:            +{(trained_acc - base_acc):.1%}")
