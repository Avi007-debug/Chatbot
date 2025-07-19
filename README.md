<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Chatbot Project README</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 2em; background: #f9f9f9; line-height: 1.6; color: #333; }
    h1, h2, h3 { color: #2c3e50; }
    code { background: #eee; padding: 2px 5px; border-radius: 4px; }
    pre { background: #eee; padding: 10px; border-radius: 6px; overflow-x: auto; }
    ul { list-style: disc; padding-left: 20px; }
    .code-block { background-color: #f4f4f4; padding: 10px; border-radius: 5px; }
  </style>
</head>
<body>

<h1>🤖 Chatbot — Flask & Streamlit + OpenAI</h1>
<p>An intelligent chatbot application built using <strong>Flask</strong>, <strong>Streamlit</strong>, and the <strong>OpenAI API</strong>. Choose between:</p>
<ul>
  <li>A <strong>Flask-based</strong> web chat interface</li>
  <li>A <strong>Streamlit</strong> interactive chat experience</li>
</ul>

<p>Inspired by similar projects like “OpenAI Simple Chat”.</p>

<h2>🚀 Features</h2>
<ul>
  <li>🧠 <strong>GPT‑powered responses</strong>: Connects to OpenAI’s GPT‑3.5 or GPT‑4 for dynamic conversations</li>
  <li>💻 <strong>Flask UI</strong>: Full-stack web chat accessible via HTML templates</li>
  <li>⚡ <strong>Streamlit UI</strong>: Lightweight, Pythonic chat interface with minimal setup</li>
  <li>📝 <strong>Downloadable transcripts</strong>: Export chat logs as markdown/text</li>
  <li>⚙️ <strong>Customizable prompts</strong>: Configure system/user prompts and model parameters</li>
</ul>

<h2>⚒️ Tech Stack</h2>
<ul>
  <li>Python 3.8+</li>
  <li>Flask</li>
  <li>Streamlit</li>
  <li>OpenAI Python SDK</li>
  <li>dotenv (for secure environment variables)</li>
</ul>

<h2>📦 Installation</h2>
<pre><code>git clone https://github.com/Avi007-debug/Chatbot.git
cd Chatbot

pip install -r requirements.txt
</code></pre>

<p>Create a <code>.env</code> file and add your OpenAI API key:</p>
<pre><code>OPENAI_API_KEY=your_openai_key_here
</code></pre>

<h2>🧭 Usage Options</h2>

<h3>🔌 Flask version</h3>
<pre><code>python flask_app.py</code></pre>
<p>Access via: <a href="http://localhost:5000/">http://localhost:5000/</a></p>

<h3>⚡ Streamlit version</h3>
<pre><code>streamlit run streamlit_app.py</code></pre>
<p>Opens on: <a href="http://localhost:8501/">http://localhost:8501/</a></p>

<h2>✨ Configuration</h2>
<ul>
  <li><strong>Model & Parameters</strong>: Set <code>OPENAI_MODEL</code> in <code>.env</code> (e.g., <code>"gpt-3.5-turbo"</code>)</li>
  <li><strong>Prompt Tuning</strong>: Adjust system/user prompts inside the app scripts</li>
</ul>

<h2>🗂️ Project Structure</h2>
<pre><code>Chatbot/
├── flask_app.py           # Flask backend + chat handlers
├── templates/             # HTML templates for chat UI
│   └── chat.html
├── streamlit_app.py       # Streamlit-based chat interface
├── requirements.txt
├── .env.example
└── README.md
</code></pre>

<h2>🪄 Extend & Customize</h2>
<ul>
  <li>🔧 Add user sessions to retain chat history</li>
  <li>🧠 Integrate LangChain or retrieval-based prompting</li>
  <li>🛠️ Deploy using Docker, Heroku, Vercel, or Streamlit Cloud</li>
  <li>🎨 Customize UI with CSS, emoji support, file input</li>
</ul>

<h2>🎯 Ideal For</h2>
<ul>
  <li>Prototyping an AI-powered conversational system</li>
  <li>Quick demos and internal tools</li>
  <li>Learning or teaching full-stack AI integration</li>
</ul>

<h2>🏁 Want More?</h2>
<p>Let me know if you'd like:</p>
<ul>
  <li>🧩 Flask API + Streamlit UI hybrid setup</li>
  <li>📦 Docker deployment files</li>
  <li>🧬 LangChain or RAG enhancements</li>
</ul>

</body>
</html>

