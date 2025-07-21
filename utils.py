import streamlit as st
from groq import Groq
from prompts import get_prompt

client = Groq(api_key=st.secrets["groq"]["api_key"])

def query_openai(user_input):
    prompt = get_prompt(user_input)
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful movie recommendation assistant."},
            {"role": "user", "content": prompt},
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
