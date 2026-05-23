# problems.py
# ML engineering questions with exact verifiable answers.
# Rule: answers must be checkable without human judgment.

ML_PROBLEMS = [
    {
        "question": "What activation function squashes input to a value strictly between 0 and 1? Answer in one word.",
        "answer": "sigmoid",
        "category": "activations"
    },
    {
        "question": "In a neural network, what does a ReLU activation return for an input of -5? Answer with just the number.",
        "answer": "0",
        "category": "activations"
    },
    {
        "question": "What does 'overfitting' mean in terms of bias and variance? Answer: high bias or high variance?",
        "answer": "high variance",
        "category": "fundamentals"
    },
    {
        "question": "What optimizer combines momentum with adaptive learning rates per parameter? Answer in one word.",
        "answer": "adam",
        "category": "optimizers"
    },
    {
        "question": "In gradient descent, if training loss keeps increasing, should you increase or decrease the learning rate? One word answer.",
        "answer": "decrease",
        "category": "training"
    },
    {
        "question": "What technique randomly zeros out neurons during training to prevent overfitting? Answer in one word.",
        "answer": "dropout",
        "category": "regularization"
    },
    {
        "question": "What is the output of softmax guaranteed to sum to? Answer with just the number.",
        "answer": "1",
        "category": "activations"
    },
    {
        "question": "What normalization technique normalizes activations across the batch dimension? Answer in two words.",
        "answer": "batch normalization",
        "category": "normalization"
    },
    {
        "question": "In classification, which loss function is standard for multi-class problems? Answer: MSE or cross-entropy?",
        "answer": "cross-entropy",
        "category": "loss_functions"
    },
    {
        "question": "What does the 'learning rate scheduler' do during training? Answer: increases, decreases, or adjusts the learning rate?",
        "answer": "adjusts",
        "category": "training"
    },
    {
        "question": "If a model has high training accuracy but low validation accuracy, is it underfitting or overfitting?",
        "answer": "overfitting",
        "category": "fundamentals"
    },
    {
        "question": "What operation in a transformer allows each token to attend to every other token? Answer in two words.",
        "answer": "self attention",
        "category": "transformers"
    },
    {
        "question": "Which layer in a transformer uses the feed-forward network? Answer: attention layer or FFN layer?",
        "answer": "ffn",
        "category": "transformers"
    },
    {
        "question": "What is the purpose of weight decay in training? Answer: reduces overfitting or underfitting?",
        "answer": "overfitting",
        "category": "regularization"
    },
    {
        "question": "In backpropagation, which direction do gradients flow? Answer: forward or backward?",
        "answer": "backward",
        "category": "fundamentals"
    },
]

def get_prompts():
    """Format problems as chat-style prompts for the LLM."""
    prompts = []
    for p in ML_PROBLEMS:
        prompt = f"""You are an expert ML engineer. Answer the following question concisely and accurately.

Question: {p['question']}

Answer:"""
        prompts.append({
            "prompt": prompt,
            "answer": p["answer"],
            "category": p["category"]
        })
    return prompts
