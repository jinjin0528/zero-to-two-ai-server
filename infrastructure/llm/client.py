from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt: str, model="gpt-4.1", temperature: float = 0.2):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a real estate assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )

    return response.choices[0].message.content
