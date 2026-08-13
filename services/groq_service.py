from groq import Groq
from groq import RateLimitError
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


class GroqService:

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found in .env file"
        )

    client = Groq(
        api_key=api_key
    )

    model = os.getenv(
        "GROQ_MODEL",
        "llama-3.1-8b-instant"
    )

    @staticmethod
    def chat(prompt: str):

        try:

            response = GroqService.client.chat.completions.create(
                model=GroqService.model,
                temperature=0.1,
                max_tokens=1000,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.choices[0].message.content

        except RateLimitError:

            return """
⚠️ Groq Daily Token Limit Reached

Your Groq quota has been exhausted.

Options:
• Wait for reset
• Use another API key
• Upgrade Groq account
• Reduce prompt size
"""

        except Exception as e:

            return f"Groq Error: {str(e)}"