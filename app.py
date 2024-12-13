import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Add custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 18px;
        color: #333;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .result-box {
        font-size: 18px;
        padding: 15px;
        border-radius: 10px;
        background-color: #f1f1f1;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Google Translator</div>', unsafe_allow_html=True)

# Input text area
st.markdown('<p class="subtitle">Enter the text you want to translate:</p>', unsafe_allow_html=True)
user_input = st.text_area("", placeholder="Type here...")

# Dropdown for target languages
st.markdown('<p class="subtitle">Select the target language:</p>', unsafe_allow_html=True)
target_language = st.selectbox(
    "Choose a language",
    options=list(LANGUAGES.values()),
    index=list(LANGUAGES.values()).index("english")  # Default to English
)

if user_input and target_language:
    # Find the target language code
    target_language_code = [key for key, value in LANGUAGES.items() if value == target_language][0]
    # Add a button to trigger translation
if st.button("Translate"):
    if user_input and target_language:
        # Find the target language code
        target_language_code = [key for key, value in LANGUAGES.items() if value == target_language][0]
    # Translate the text
    try:
        translation = translator.translate(user_input, dest=target_language_code)
        st.markdown('<p class="subtitle">Translated Text:</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="result-box">{translation.text}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")
