from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def analyze_log_anomaly(log_file_path: str) -> str:

    with open(log_file_path, "r") as log_file:
        log_content = log_file.read()

    prompt = (
        f"""
        You are a technical auditor who has to analyze the log file: {log_content} focusing only on the [CRITICAL] entries and providing as output a summary divided in two parts: 1) The error type, and 2) The immediate impact.
        Be precise and factual
        Print only the summary.
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
        max_tokens=80,
        temperature=0.1,
    )
    return response.choices[0].message.content

def main():
    print(analyze_log_anomaly("/root/openaiproject/app.log"))

if __name__ == "__main__":
    main()