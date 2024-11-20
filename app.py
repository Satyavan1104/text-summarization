import streamlit as st
import cohere

# Initialize the Cohere client with your API key
api_key = 'Mrh9BFF0YcKhl4jp5JC7ijKj0JwpQXdKFiz2aWm4'  # Replace this with your actual Cohere API key
co = cohere.Client(api_key)

# Streamlit App
def summarize_text(text, length='short'):
    # Summarize the input text using Cohere API
    response = co.summarize(
        text=text,
        length=length  # 'short', 'medium', 'long'
    )
    return response.summary

# Streamlit UI
st.title("Text Summarization with Cohere")

# Input box for the user to provide the text they want to summarize
input_text = st.text_area("Enter your text here (min 20 characters):", height=20)

# Option for the user to select summary length
summary_length = st.selectbox(
    "Select summary length:",
    ("short", "medium", "long")
)

# Button to trigger the summarization
if st.button("Summarize"):
    if len(input_text.strip()) < 20:
        st.warning("Please enter at least 20 characters of text.")
    else:
        summary = summarize_text(input_text, length=summary_length)
        st.subheader("Summary:")
        st.write(summary)
