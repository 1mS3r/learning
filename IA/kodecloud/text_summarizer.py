from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def summarize(text: str) -> str:
    prompt = (
        f"""
        You are an expert communicator tasked with writing a summary of the following text:{text}. Please ensure that the resulting summary is concise, clear, and is limited to a single line.
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
        temperature=0.5,
    )
    return response.choices[0].message.content

def main():
    print(summarize("Artificial Intelligence enables machines to mimic human intelligence, performing tasks such as learning, problem-solving, and decision-making with increasing accuracy."))

if __name__ == "__main__":
    main()