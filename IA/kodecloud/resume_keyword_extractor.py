from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def extract_keywords(text: str) -> str:
    prompt = (
        f"""
        You are an expert communicator tasked with extracting key skills and experiences from the following resume text: {text}, and returning them as a comma-separated list of keywords. Please ensure that the extracted keywords are relevant and concise while maintaining the number in exactly 5.
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
        max_tokens=40,
        temperature=0,
    )
    return response.choices[0].message.content

def main():
    print(extract_keywords("Experienced DevOps engineer skilled in Python, Kubernetes, Docker, CI/CD pipelines, and cloud automation."))

if __name__ == "__main__":
    main()