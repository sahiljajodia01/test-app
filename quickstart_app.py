import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load API keys from .env file (optional but recommended)
load_dotenv()

# Initialize LLM (replace with your preferred model)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-8b", google_api_key=os.environ.get("GOOGLE_API_KEY"))  # Use os.environ if not using .env
# Create a prompt template
template = """
You are a helpful AI assistant that answers questions based on the following context:

{context}

Question: {question}
Answer:"""
prompt = PromptTemplate(template=template, input_variables=["context", "question"])

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit UI
st.title("Question Answering with LangChain")

# Context input
context = st.text_area("Enter the context:", height=200)

# Question input
question = st.text_input("Enter your question:")

# Run the chain when the user clicks the button
if st.button("Get Answer"):
    if context and question:
        with st.spinner("Thinking..."):
            # Run the chain
            response = chain.run({"context": context, "question": question})

            # Display the response
            st.write(response)
    else:
        st.error("Please provide both context and a question.")