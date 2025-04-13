import streamlit as st
import openai

# ✅ Set Groq API Key securely
openai.api_key = "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"
openai.base_url = "https://api.groq.com/openai/v1"

# ✅ Page config
st.set_page_config(page_title="LLaMA Chatbot", layout="centered")
st.title("🤖 Jilu's first LLaMA Chatbot via Groq")
st.write("Ask anything and get answers powered by LLaMA on Groq!")

# ✅ Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful AI chatbot."}]

# ✅ Display chat history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# ✅ User input box
user_input = st.chat_input("Type your message here...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        try:
            response = openai.chat.completions.create(
                model="llama3-8b-8192",  # or use "llama3-70b-8192"
                messages=st.session_state.messages
            )
            assistant_reply = response.choices[0].message.content
            st.chat_message("assistant").markdown(assistant_reply)
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
        except Exception as e:
            st.error(f"Something went wrong: {e}")
