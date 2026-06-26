from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def clarify_bug(description: str) -> str:
    prompt = (
        f"""
        You are an expert communicator tasked with writing a summary of the following informal bug reports:{description}. Please ensure that the resulting summary is clear, structured, and professional.
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
        max_tokens=100,
        temperature=0,
    )
    return response.choices[0].message.content

def main():
    print(clarify_bug("App keeps crashing when I click save."))

if __name__ == "__main__":
    main()