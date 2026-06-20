from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

def translate_to_language(text: str, language: str) -> str:
    prompt = (
        f"""
        You are an expert communicator tasked with translating the following text into {language}: {text}. Please ensure that the translation is accurate and natural-sounding.
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
        temperature=0.7,
    )
    return response.choices[0].message.content

def main():
    print("Spanish Translation:")
    print(translate_to_language("Good morning, how are you?", "Spanish"))

    print("\nFrench Translation:")
    print(translate_to_language("Good morning, how are you?", "French"))


if __name__ == "__main__":
    main()