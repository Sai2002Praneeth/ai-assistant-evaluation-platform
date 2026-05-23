from groq import Groq
from app.memory.conversation_memory import ConversationMemory
import os


class OSSAssistant:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.memory = ConversationMemory()

    def generate_response(self, user_input):
        self.memory.add_message("user", user_input)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful open-source AI assistant. "
                    "Maintain conversational context and answer clearly."
                ),
            }
        ]

        messages.extend(self.memory.get_messages())

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
        )

        response = completion.choices[0].message.content

        self.memory.add_message("assistant", response)

        return response