from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class OSSAssistant:
    def __init__(self):
        self.model_name = "Qwen/Qwen2.5-0.5B-Instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float32
        )

    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=100
        )

        response = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return response