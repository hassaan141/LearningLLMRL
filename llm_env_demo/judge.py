# judge.py
# The judge/reward function.
# Takes the LLM's output and the correct answer.
# Returns a score between 0.0 and 1.0.

import re


def normalize(text: str) -> str:
    """Clean up text for fair comparison."""
    text = text.lower().strip()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text)
    return text


def judge(llm_output: str, correct_answer: str) -> float:
    """
    Score the LLM's output against the correct answer.

    Returns:
        1.0  — correct answer found in output (pass)
        0.0  — correct answer not found (fail)

    Design notes:
        - We use 'contains' not 'equals' to handle verbosity
          e.g. "The answer is sigmoid" still scores 1.0
        - We normalize both strings to avoid case/punctuation issues
        - Binary scoring keeps it simple and unambiguous
    """
    output_normalized = normalize(llm_output)
    answer_normalized = normalize(correct_answer)

    if answer_normalized in output_normalized:
        return 1.0

    return 0.0


def batch_judge(outputs: list[str], answers: list[str]) -> list[float]:
    """Judge a batch of outputs at once (used by GRPO trainer)."""
    return [judge(o, a) for o, a in zip(outputs, answers)]


# Quick test — run this file directly to verify
if __name__ == "__main__":
    test_cases = [
        ("The answer is sigmoid", "sigmoid", 1.0),
        ("sigmoid", "sigmoid", 1.0),
        ("Sigmoid activation", "sigmoid", 1.0),
        ("relu", "sigmoid", 0.0),
        ("The output is 0 for negative inputs", "0", 1.0),
        ("high variance", "high variance", 1.0),
        ("This is overfitting, which means high variance", "high variance", 1.0),
        ("I don't know", "sigmoid", 0.0),
    ]

    print("Judge Tests:")
    print("-" * 50)
    all_passed = True
    for output, answer, expected in test_cases:
        score = judge(output, answer)
        status = "✓" if score == expected else "✗ FAILED"
        print(f"{status} | Output: '{output[:30]}' | Expected: {expected} | Got: {score}")
        if score != expected:
            all_passed = False

    print("-" * 50)
    print("All tests passed!" if all_passed else "Some tests failed!")
