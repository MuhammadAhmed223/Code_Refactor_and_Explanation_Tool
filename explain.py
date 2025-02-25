import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("RAG_KEY")
)

def explain_code(code):
    """Generates an explanation for the given Python code using OpenRouter API."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",
            messages=[
                {"role": "system", "content": "You are a helpful AI that explains Python code in detail."},
                {"role": "user", "content": f"Explain the following Python code:\n\n{code}"}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"
