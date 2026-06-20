from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def compare(item1: str, item2: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": (
                    f"""
                    You are a senior mobile analyst tasked to generate a brief and clear response comparing only
                    the chipset of those 2 devices: {item1} and {item2}
                    """
                )
            }
        ],
        max_tokens=100,
        temperature=0.5,
    )
    return response.choices[0].message.content

def main():
    print(compare("iphone 13", "iphone 17"))

if __name__ == "__main__":
    main()