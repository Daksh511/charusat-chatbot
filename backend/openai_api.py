import openai
from config import OPENAI_API_KEY, OPENAI_API_BASE, GPT_MODEL

openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_API_BASE

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model=GPT_MODEL,
        messages=[{"role": "system", "content": "You are an AI assistant for CHARUSAT college inquiries."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
