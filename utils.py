import streamlit as st
import json
from groq import Groq
from prompts import base_prompt

client = Groq(api_key=st.secrets["groq"]["api_key"])

def query_openai(prompt):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You're a movie expert who assigns characters to personalities."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def build_prompt(name, personality):
    return f"""
Act as a movie and series expert. A user named {name} just shared their personality:
"{personality}"

You must ONLY suggest real fictional characters from Indian Cinema (Bollywood) or Korean Dramas (K-dramas).

Rules:
- Give ONE best-match fictional character only
- Include the correct show or movie name
- Mention actor name only if certain; otherwise say "Unknown"
- If unsure, say "I am not sure" — do not make things up

Format:
Character: [Name]
Show/Movie: [Title]
Actor: [Optional]
Reason: [reason why they're a match]
Suggestions: [suggest any 2 movies or series which matches the vibe]
"""