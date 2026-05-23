from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class OSSAssistant:

    def __init__(self):

        self.model_name = "Qwen/Qwen2.5-0.5B-Instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float32
        )

        self.device = "cpu"

        self.model.to(self.device)

    def generate_response(self, prompt, history=None):

        messages = [
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        ]

        if history:
            messages.extend(history)

        messages.append({
            "role": "user",
            "content": prompt
        })

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=120,
            temperature=0.7
        )

        generated_ids = outputs[0][inputs["input_ids"].shape[1]:]

        response = self.tokenizer.decode(
            generated_ids,
            skip_special_tokens=True
        )

        return response.strip()