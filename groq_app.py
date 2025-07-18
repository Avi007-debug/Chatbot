import os
import time
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Endpoint and model details
url = "https://api.groq.com/openai/v1/chat/completions"
model = "llama3-8b-8192"

def generate_blog(paragraph_topic):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"Write a detailed paragraph about the topic: {paragraph_topic}"
            }
        ],
        "temperature": 0.5,
        "max_tokens": 400
    }

    for attempt in range(3):  # Retry up to 3 times
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        
        except requests.exceptions.HTTPError as err:
            if response.status_code == 429:
                print("⚠️ Rate limit hit. Waiting 10 seconds before retrying...")
                time.sleep(10)
            elif response.status_code in [401, 403]:
                print("🔐 API key is missing,invalid, expired. Check your .env file.")
                break
            else:
                print(f"❌ HTTP Error: {err}")
                break
        except Exception as e:
            print(f"❗ Unexpected error: {e}")
            break

    return "❌ Failed to generate paragraph after multiple attempts."

# Interactive loop to generate multiple paragraphs
def main():
    print("📝 Blog Generator (Groq + LLaMA3)")
    keep_writing = True

    while keep_writing:
        answer = input("Write a paragraph? (Y for yes, anything else for no): ").strip()
        if answer.upper() == "Y":
            paragraph_topic = input("What should this paragraph talk about? ").strip()
            print("\n⏳ Generating paragraph...\n")
            result = generate_blog(paragraph_topic)
            print(result)
            print("\n" + "-" * 50 + "\n")
        else:
            keep_writing = False
            print("👋 Exiting. Happy blogging!")

if __name__ == "__main__":
    main()
