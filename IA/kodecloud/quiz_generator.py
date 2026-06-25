from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

def generate_quiz(topic: str) -> str:
    prompt = f"""
You are a quiz generator. Generate exactly one multiple-choice question (MCQ) on the topic: {topic}.
Respond following exactly this JSON format:
[
  {{
    "question": "The question text.",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "The correct answer text."
  }}
]
"""
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.3,
    )
    return response.choices[0].message.content

def main():
    print(generate_quiz("Basic Linux Commands"))

if __name__ == "__main__":
    main()
