import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI

# Load environment variables (retrieves the API key if a .env file exists)
load_dotenv(override=True)

# ----------------------------------------------------
# 1. PROVIDER CONFIGURATION (Switch model via USE_OLLAMA flag)
# ----------------------------------------------------

USE_OLLAMA = True

if USE_OLLAMA:
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"  # Yerel model şifre istemez
    )
    MODEL_NAME = "llama3.2"
else:
    client = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=os.getenv("GEMINI_API_KEY")
    )
    MODEL_NAME = "models/gemini-3.7-flash"

# ----------------------------------------------------
# 2. PROMPT TEMPLATES
# ----------------------------------------------------
SYSTEM_PROMPT = """
You’re a witty AI assistant. Answer questions with a joke.
"""

USER_PROMPT_PREFIX = """
Here is the content of a website. Summarize the website:
"""

def messages_for(website_content):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT_PREFIX + website_content}
    ]

# ----------------------------------------------------
# 3. SUMMARIZATION PIPELINE
# ----------------------------------------------------
def summarize(url):
    print(f"[{MODEL_NAME}] ile web sitesi taranıyor: {url}...")
    website_text = fetch_website_contents(url)
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages_for(website_text)
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    target_url = "https://docs.python.org/3/"
    result = summarize(target_url)
    print("\n--- ÖZET ---\n")
    print(result)