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

    def generate_response(self, prompt, history=None):

        conversation = ""

        if history:
            for msg in history:
                role = msg["role"]
                content = msg["content"]

                conversation += f"{role}: {content}\n"

        conversation += f"user: {prompt}\nassistant:"

        inputs = self.tokenizer(
            conversation,
            return_tensors="pt"
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=100,
            temperature=0.7,
            do_sample=True
        )

        response = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        # Clean assistant response
        if "assistant:" in response:
            response = response.split("assistant:")[-1].strip()

        return response