from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def convert_to_bullets(text: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": (
                    f"""
                    You are an expert communicator tasked with converting the following text into a clear and concise bullet point list: {text}
                    """
                )
            }
        ],
        max_tokens=150,
        temperature=0.1,
    )
    return response.choices[0].message.content

def main():
    print(convert_to_bullets("Artificial Intelligence is transforming industries by automating tasks, improving decision-making, and enabling new innovations across healthcare, finance, and education."))

if __name__ == "__main__":
    main()