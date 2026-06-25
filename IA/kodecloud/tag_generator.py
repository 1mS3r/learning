from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

def generate_seo(description: str, tone: str) -> str:
    prompt = f"""
You are a creative SEO & Marketing specialist. Generate titles and SEO-optimized keyword sets for product listings, helping businesses reach the right audience effectively.
For this, Generate a short, attention-grabbing product title (4-8 words) in the specified tone. {tone} using the provided description for context: {description}.
Generate exactly ten low-competition keywords, separated by commas, for SEO tagging.
Respond following exactly this format:
Line 1: The generated title.
Line 2: The ten comma-separated keywords.

"""
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=60,
        temperature=0.7,
    )
    return response.choices[0].message.content

def main():
    print(generate_seo("A waterproof, lightweight backpack designed for multi-day hikes in difficult terrain.", 'Rugged and Adventurous'))

if __name__ == "__main__":
    main()
