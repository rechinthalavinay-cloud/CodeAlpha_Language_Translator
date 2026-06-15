import streamlit as st
from deep_translator import GoogleTranslator

# Page Settings
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 AI Language Translation Tool")

# Language Dictionary
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko"
}

# Source Language
source_lang = st.selectbox(
    "Source Language",
    list(languages.keys())
)

# Target Language
target_lang = st.selectbox(
    "Target Language",
    list(languages.keys())
)

# Input Text
text = st.text_area(
    "Enter Text",
    height=150
)

# Translate Button
if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text to translate.")

    else:
        try:
            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.success("Translation Complete!")

            st.subheader("Translated Text")

            st.text_area(
                "",
                translated,
                height=150
            )

        except Exception as e:
            st.error(f"Error: {e}")