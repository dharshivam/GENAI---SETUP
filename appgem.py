import google.generativeai as genai
import streamlit as st
import os

# Get the API key from environment variable
key = os.getenv('GOOGLE_API_KEY')

# Configure the API key
genai.configure(api_key=key)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# Create a frontend UI using streamlit
st.title("SIMPLE TEXT GENERATION USING GEMINI")
st.header("This is to test the gemini model as application")

prompt = st.text_area("Write your prompt here", max_chars=10000)

if st.button("Generate"):
    if prompt.strip():  # make sure it's not empty
        response = model.generate_content(prompt)
        st.write(response.text)
    else:
        st.warning("⚠️ Please enter a prompt before generating.")
