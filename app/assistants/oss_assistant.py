from groq import Groq
from memory.conversation_memory import ConversationMemory
import os


class OSSAssistant:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.memory = ConversationMemory()

    def generate_response(
        self,
        prompt,
        history=None
    ):

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful open-source AI assistant."
                )
            }
        ]

        if history:

            for msg in history:

                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })

        messages.append({
            "role": "user",
            "content": prompt
        })

        completion = (
            self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.7
            )
        )

        response = (
            completion
            .choices[0]
            .message.content
        )

        return response