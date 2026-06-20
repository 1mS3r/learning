from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def generate_haiku(topic: str) -> str:
    prompt = (
        f"""
        You are an expert poet tasked with writing a haiku about:{topic}. Please ensure that the haiku follows the traditional 5-7-5 syllable structure and captures the essence of the topic in a concise and evocative manner.
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
    print(generate_haiku("sky"))

if __name__ == "__main__":
    main()