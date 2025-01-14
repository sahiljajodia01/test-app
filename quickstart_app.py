import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

# Initialize LLM (replace with your preferred model)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-8b", google_api_key=st.secrets["GOOGLE_API_KEY"])  # Use os.environ if not using .env
# Create a prompt template
template = """
Please help me plan a travel itinerary for {country_name} for {number_of_days} days. Create a day-by-day plan that includes recommended activities, must-see attractions, dining options, and tips for transportation. Optimize the itinerary to make the most of the time available.
"""
prompt = PromptTemplate(template=template, input_variables=["country_name", "number_of_days"])

# Create a chain
chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit UI
st.title("Travel planer app")

# Country input
country_name = st.text_input("Enter a country name:")

# Days input
number_of_days = st.text_input("Enter the number od days you want to travel")

# Run the chain when the user clicks the button
if st.button("Get itineraries"):
    if country_name and number_of_days:
        with st.spinner("Thinking..."):
            # Run the chain
            response = chain.run({"country_name": country_name, "number_of_days": number_of_days})

            # Display the response
            st.write(response)
    else:
        st.error("Please provide both country_name and a number_of_days.")