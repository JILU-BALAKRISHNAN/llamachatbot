import streamlit as st
import os
from openai import OpenAI

# --- Set your Groq API Key here ---
GROQ_API_KEY = "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"
  # Replace with your key
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

st.set_page_config(page_title="LLaMA Chatbot", layout="centered")

st.title("🤖 LLaMA Chatbot via Groq")
st.write("Ask anything and get answers powered by LLaMA on Groq!")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful AI chatbot."}]

# Display chat history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message here...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="llama3-8b-8192",  # Or try llama3-70b-8192
                messages=st.session_state.messages
            )
            assistant_reply = response.choices[0].message.content
            st.chat_message("assistant").markdown(assistant_reply)
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        except Exception as e:
            st.error(f"Something went wrong: {e}")
