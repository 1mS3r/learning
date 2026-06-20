from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def chatbot_call(prompt: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": (
                     prompt
                )
            }
        ],
        max_tokens=100,
        temperature=0.7,
    )
    return response.choices[0].message.content

def main():
    print(chatbot_call("You are a friendly travel guide. Greet the user and ask where they want to go."))

if __name__ == "__main__":
    main()