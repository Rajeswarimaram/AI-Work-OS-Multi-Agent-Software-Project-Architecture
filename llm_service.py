import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in the .env file.")
groq_client = Groq(
    api_key=GROQ_API_KEY
)

def generate_response(user_prompt: str) -> str:
    """Sends a prompt to the Groq LLM
    and returns the generated response."""
    print("USING GROQ LLM")
    try:
        ai_response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.4,
             max_tokens=1024
        )
        return ai_response.choices[0].message.content
    except Exception as error:
        return f"Groq Error:\n{error}"