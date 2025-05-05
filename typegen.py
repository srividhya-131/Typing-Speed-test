import streamlit as st
import random
import time

# Sample sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a fun programming language.",
    "Typing speed matters for productivity.",
    "Practice makes a person perfect.",
    "Code daily to sharpen your skills."
]

# Initialize session state
if 'sentence' not in st.session_state:
    st.session_state.sentence = random.choice(sentences)
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0.0
if 'test_started' not in st.session_state:
    st.session_state.test_started = False

st.title("Typing Speed Test")

# Start Test button
if st.button("Start Test"):
    st.session_state.sentence = random.choice(sentences)
    st.session_state.start_time = time.time()
    st.session_state.test_started = True

if st.session_state.test_started:
    st.markdown("*Type the following sentence:*")
    st.code(st.session_state.sentence)

    typed_text = st.text_input("Start typing here...")

    if st.button("Submit"):
        end_time = time.time()
        time_taken = round(end_time - st.session_state.start_time, 2)
        word_count = len(typed_text.split())
        wpm = round(word_count / (time_taken / 60), 2) if time_taken > 0 else 0

        if typed_text.strip() == st.session_state.sentence.strip():
            st.success(f"Correct! Time: {time_taken} seconds | Speed: {wpm} WPM")
        else:
            st.error("Text does not match! Please try again.")


