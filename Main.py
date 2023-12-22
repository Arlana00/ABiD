import streamlit as st
import google.generativeai as genai
from api import api

# Configure the API key
genai.configure(api_key=api)

# Set default parameters
defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}

st.title('Assistan Code Writer')
st.write('You can ask me to code anything')
final_response = None

# Creating a side panel for inputs
with st.sidebar:
    st.write("## Code Generator Settings")
    # Create a dropdown for selecting the programming language
    programming_language = st.selectbox("Choose the programming language:", 
                                        ["Python", "C", "JavaScript", "Java"])
    # Create a text input for the prompt
    prompt = st.text_input("What do you want to code?")
    # When the 'Generate' button is pressed, generate the text
    if st.button('Generate'):
        formatted_prompt = f"Write a {programming_language.lower()} code about {prompt}"
        response = genai.generate_text(
            **defaults,
            prompt=formatted_prompt
        )
        final_response = response

# Display the generated code
if final_response is not None:
    st.write(final_response.result)
    
    if programming_language == "Python":
            file_extension = "py"
    elif programming_language == "C":
        file_extension = "c"
    elif programming_language in ["JavaScript"]:
        file_extension = "js"
    elif programming_language in ["Java"]:
        file_extension = "java"    
    else:
        file_extension = "txt"
    # Add a download button
    download_button = st.download_button(
        label="Download Code",
        data=final_response.result.encode('utf-8'),
        file_name=f"generated_code.{file_extension}"
    )
