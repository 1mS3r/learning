from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def analyze_sentiment(text: str) -> str:
    prompt = (
        f"""
        You are a sentiment analysis tool. Analyze the sentiment of the following text: {text} and respond following exactly this format:
        Sentiment:<Positive/Negative/Neutral>
        Reason:<short explanation>
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
        temperature=0.0,
    )
    return response.choices[0].message.content

def main():
    print(analyze_sentiment("I am really happy with the new update!"))

if __name__ == "__main__":
    main()