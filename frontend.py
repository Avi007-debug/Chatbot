import os
import time
import requests
import streamlit as st
from dotenv import load_dotenv
from io import StringIO

# Load .env and API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
model = "llama3-8b-8192"
url = "https://api.groq.com/openai/v1/chat/completions"

# Function to call Groq API
def generate_paragraph(topic, count=1):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    all_paragraphs = ""
    for i in range(count):
        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": f"Write a detailed paragraph about: {topic}"}
            ],
            "temperature": 0.5,
            "max_tokens": 400
        }

        for attempt in range(3):
            try:
                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()
                paragraph = response.json()["choices"][0]["message"]["content"]
                all_paragraphs += f"\n\n[{i+1}] {paragraph.strip()}"
                break
            except requests.exceptions.HTTPError as err:
                if response.status_code == 429:
                    time.sleep(10)
                elif response.status_code in [401, 403]:
                    return "🔐 Invalid or missing API key. Check your .env file."
                else:
                    return f"❌ HTTP Error: {err}"
            except Exception as e:
                return f"❗ Error: {e}"

    return all_paragraphs.strip()

# -------------------- Streamlit UI --------------------

st.set_page_config(page_title="Groq Blog Generator", page_icon="📝")

with st.sidebar:
    st.title("📝 Blog Generator")
    st.markdown("Powered by **Groq** + **LLaMA3**")
    dark_mode = st.toggle("🌙 Dark Mode", value=True)
    st.markdown("---")
    st.markdown("Developed with ❤️ using Streamlit")

# Apply custom dark/light theme (if needed in the future)

st.title("🚀 AI-Powered Blog Paragraph Generator")

if not api_key:
    st.error("❌ GROQ_API_KEY not found in your .env file.")
    st.stop()

# --- Input Form ---
with st.form("blog_form"):
    topic = st.text_input("📌 Enter a blog topic:", placeholder="e.g., Green Energy Solutions")
    para_count = st.slider("📝 Number of paragraphs", 1, 5, value=1)
    submit = st.form_submit_button("Generate 🚀")

# --- Generation Result ---
if submit:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic before generating.")
    else:
        with st.spinner("⏳ Generating paragraph(s)..."):
            output = generate_paragraph(topic, count=para_count)

        if "Error" in output or "Invalid" in output:
            st.error(output)
        else:
            st.success("✅ Content generated successfully!")
            st.markdown("### ✨ Generated Blog Paragraph(s):")
            st.write(output)

            # Download as .txt
            txt_buffer = StringIO(output)
            st.download_button(
                label="📥 Download as .txt",
                data=txt_buffer.getvalue(),
                file_name=f"{topic.replace(' ', '_')}_blog.txt",
                mime="text/plain"
            )
