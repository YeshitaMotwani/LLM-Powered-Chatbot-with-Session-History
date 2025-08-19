import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY_2")

# Initialize model
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Streamlit App
st.set_page_config(page_title="LLM Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 LLM Powered Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    # Build message list for model
    chat_history = []
    for m in st.session_state.messages:
        if m["role"] == "user":
            chat_history.append(HumanMessage(content=m["content"]))
        else:
            chat_history.append(AIMessage(content=m["content"]))

    # Get response from model
    response = model.invoke(chat_history)
    answer = response.content

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").markdown(answer)
