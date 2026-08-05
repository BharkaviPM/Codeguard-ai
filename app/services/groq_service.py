from groq import Groq

from app.core.config import GROQ_API_KEY


class GroqService:

    _client = None

    @classmethod
    def client(cls):

        if cls._client is None:

            cls._client = Groq(
                api_key=GROQ_API_KEY
            )

        return cls._client

    @classmethod
    def chat(
        cls,
        prompt,
        model="llama-3.3-70b-versatile"
    ):

        response = cls.client().chat.completions.create(

            model=model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.2,

            max_tokens=2048,

        )

        return response.choices[0].message.content