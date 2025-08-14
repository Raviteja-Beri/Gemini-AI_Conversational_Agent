# Chat-App with history - Gemini AI
from dotenv import load_dotenv
import streamlit as st
import os
import textwrap
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(question)

    if response.candidates and response.candidates[0].content.parts:
        return "".join(
            [part.text for part in response.candidates[0].content.parts if hasattr(part, 'text')]
        )
    else:
        return "Incorrect response from Gemini"

# Streamlit page config
st.set_page_config(page_title="Gemini AI Bot Demo")
st.header("Gemini AI Chat with History")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", key="input")

if st.button("Ask"):
    if user_input.strip():
        answer = get_gemini_response(user_input)
        st.session_state.history.append({"question": user_input, "answer": answer})

if st.session_state.history:
    for chat in reversed(st.session_state.history):
        st.markdown(f"{chat['question']}")
        st.markdown(f"{chat['answer']}")
