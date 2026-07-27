from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

st.set_page_config(page_title="Persona AI Chatbot", page_icon="🤖", layout="centered")

# Persona Definitions mapping directly to chatBot.py options
PERSONAS = {
    "Sad AI agent 😔": "you are a Sad AI agent and reply every message in sad way",
    "Happy AI agent 😊": "you are a Happy AI agent and reply every message in happy way",
    "Angry AI agent 😡": "you are a Angry AI agent and reply every message in angry way",
    "Romantic AI agent 💖": "you are a Romantic AI agent and reply every message in romantic way",
}

# Sidebar for Mode Selection
st.sidebar.title("⚙️ AI Persona Setup")
selected_persona_label = st.sidebar.radio(
    "Choose your AI Mode:",
    options=list(PERSONAS.keys()),
    index=0
)

system_prompt = PERSONAS[selected_persona_label]

# If persona changed, reset conversation history with the new SystemMessage
if "current_persona" not in st.session_state or st.session_state.current_persona != selected_persona_label:
    st.session_state.current_persona = selected_persona_label
    st.session_state.messages = [SystemMessage(content=system_prompt)]

# Clear chat button
if st.sidebar.button("🧹 Clear Conversation"):
    st.session_state.messages = [SystemMessage(content=system_prompt)]
    st.rerun()

# Page Title & Subtitle
st.title(f"🤖 {selected_persona_label}")
st.caption("Chatbot powered by Mistral AI with dynamic emotional personas")

# Initialize Chat Model
model = ChatMistralAI(model="open-mistral-7b")

# Render past chat messages (skipping system message at index 0)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Accept user input
if prompt := st.chat_input("Type your message here..."):
    # Append human message and render in UI
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get model response, render and append to message history
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
            st.markdown(response.content)
            st.session_state.messages.append(AIMessage(content=response.content))
