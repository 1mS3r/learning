from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def generate_comment(code_snippet: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": (
                    f"You are a senior software engineer tasked to generate a one-line comment explanining the following code snippet: {code_snippet}"
                )
            }
        ],
        max_tokens=30,
        temperature=0.2,
    )
    return response.choices[0].message.content

def main():
    print(generate_comment("def calculate_area(length, width): return length * width"))

if __name__ == "__main__":
    main()