from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def rewrite_email(text: str) -> str:
    prompt = (
        f"""
        You are an expert communicator tasked with rewriting the following email:{text} in a polite and professional manner. Please ensure that the rewritten email maintains the original intent while improving clarity and tone.
        """
    )
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=60,
        temperature=0.1,
    )
    return response.choices[0].message.content

def main():
    print(rewrite_email("hey send me that report asap"))

if __name__ == "__main__":
    main()