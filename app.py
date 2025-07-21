import streamlit as st
from utils import query_openai, build_prompt
from prompts import intro_text

# --- Page Config ---
st.set_page_config(page_title="CineMatch", layout="centered", page_icon="🎬")

# --- Load Custom CSS ---
with open("styles.css", "r") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

# --- App Title & Intro ---
st.markdown("<h1 class='title'>🎬 CineMatch</h1>", unsafe_allow_html=True)
st.markdown(intro_text, unsafe_allow_html=True)

# --- Input Fields ---
st.markdown("## 🔍 Discover Your On-Screen Twin")
name = st.text_input("👤 Your Name", placeholder="e.g. Sumit")
personality = st.text_area(
    "🧠 Describe your personality",
    placeholder="e.g. I'm bubbly, curious, and a bit chaotic — like a blend of Geet and Jo Yi-seo."
)

# --- Button Action ---
if st.button("🎭 Find My Character"):
    if name.strip() and personality.strip():
        with st.spinner("✨ Casting you into the reel world..."):
            prompt = build_prompt(name, personality)
            result = query_openai(prompt)
        st.success(f"🎉 You match with:\n\n**{result}**")
    else:
        st.warning("🚨 Please fill out both fields to continue.")