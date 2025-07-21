🎬 CineMatch – AI-Powered Movie Companion
CineMatch is a Streamlit-based AI app that helps users discover movies by chatting with an intelligent assistant. Built with Python, OpenAI/Groq LLMs, and Streamlit, it lets you find movie recommendations, plot summaries, genre-based suggestions, and more — all through natural language.

Live Demo: Visit on Streamlit Cloud
(Replace this link with your actual Streamlit deployment link)

🔧 Features
🎥 Chat with an AI assistant to get personalized movie recommendations

📚 Query based on genres, moods, actors, etc.

⚡ Fast response using LLMs like Groq/OpenAI

🧠 Custom prompt engineering to improve relevance

🌐 Deployed using Streamlit Cloud

🖼️ Demo
Coming soon: Add a gif or screenshot of your app UI

🚀 Tech Stack
Python

Streamlit

Groq / OpenAI API

dotenv / Streamlit secrets

📁 Project Structure
graphql
Copy
Edit
.
├── app.py                # Main Streamlit app  
├── prompts.py            # Prompt templates  
├── utils.py              # API interaction logic  
├── requirements.txt      # Python dependencies  
└── .streamlit/
    └── config.toml       # Streamlit config
🔐 Setup & Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/YourUsername/CineMatch.git  
cd CineMatch
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your API keys:

Option 1 – Using .streamlit/secrets.toml:

toml
Copy
Edit
[groq]  
api_key = "your_groq_api_key"

[openai]  
api_key = "your_openai_api_key"
Option 2 – On Streamlit Cloud:

Paste the same values in your app’s “Secrets” tab.

Run locally:

bash
Copy
Edit
streamlit run app.py
🌍 Deployment on Streamlit Cloud
Push your code to GitHub

Go to https://streamlit.io/cloud and sign in with GitHub

Click "New App", choose your repo

Add secrets under “Secrets” tab

Click "Deploy"

💡 Future Enhancements
Add mood-based recommendations

Filter by streaming platform

Save user preferences

🧑‍💻 Author
Sumit Sonawane
LinkedIn
GitHub