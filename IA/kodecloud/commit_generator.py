from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def generate_commit(changes: str) -> str:
    prompt = (
        f"""
        You are a senior developer tasked with writing a git commit message from this change message: {changes} following Conventional Commit standard - <type>: <subject>, i.e: fix: resolve issue with user authentication . Please ensure that the resulting output is just the commit message without any additional text, use less than 50 chars for the subject and maintain consistency with the input text.
        IMPORTANT: In case of doubt between more than one type, choose the most appropriate one based on the context of the change message.
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
        max_tokens=30,
        temperature=0.0,
    )
    return response.choices[0].message.content

def main():
    print(generate_commit("Added a new user registration endpoint and fixed a typo in the README file."))

if __name__ == "__main__":
    main()