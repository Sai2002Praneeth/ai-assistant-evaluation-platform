from groq import Groq
import os
import streamlit as st

from dotenv import load_dotenv

load_dotenv()


class FrontierAssistant:

    def __init__(self):

        api_key = (
            os.getenv("GROQ_API_KEY")
            or st.secrets.get(
                "GROQ_API_KEY",
                None
            )
        )

        self.client = Groq(
            api_key=api_key
        )

    def generate_response(
        self,
        prompt,
        history=None
    ):

        try:

            messages = []

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

            response = (
                self.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages,
                    temperature=0.7
                )
            )

            return (
                response
                .choices[0]
                .message.content
            )

        except Exception as e:

            return (
                f"⚠️ Error generating response: {str(e)}"
            )