import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

st.title("🦜🔗 Basic chat app")

def generate_response(input_text):
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-8b", google_api_key=os.environ.get("GOOGLE_API_KEY"))
    st.info(model.invoke(input_text).content)

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)