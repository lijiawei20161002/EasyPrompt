# EasyPrompt
Take the MMLU dataset (MATH Subset) - https://huggingface.co/datasets/cais/mmlu
For your given favorite model, find ten questions where the model 0-shot gets the answer correct.
Generate a prompt that, when used, lets the model generate convincing arguments for an incorrect answer.

Bonus points for:
1. showing this prompt generalizes to different models.
2. building a scaffold to help improve the answer
3. showing weaker models cannot detect the actual mistake in the question 
4. building a convincing classifier
