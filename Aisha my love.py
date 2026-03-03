import streamlit as st
import time

# Page config for a romantic look
st.set_page_config(page_title="For Aisha", page_icon="❤️")

# Initialize session state to track steps
if 'phase' not in st.session_state:
    st.session_state.phase = 'start'
if 'praise_index' not in st.session_state:
    st.session_state.praise_index = 0

praises = [
    "Aisha, your smile is my favorite piece of code.",
    "You are the most beautiful person in my world.",
    "I am so lucky to have you by my side.",
    "You make every day feel like a dream, Aisha.",
    "You are my queen, today and forever."
]

# Phase 1: Touching Steve's Chest
if st.session_state.phase == 'start':
    st.title("Touch Steve's Chest...")
    if st.button("❤️", help="Click here to start", use_container_width=True):
        st.session_state.phase = 'praising'
        st.balloons() # Floating effect
        time.sleep(1)
        st.rerun()

# Phase 2: The Praising Heart
elif st.session_state.phase == 'praising':
    st.title("For My Love, Aisha")
    
    # Display current phrase
    current_praise = praises[st.session_state.praise_index % len(praises)]
    st.subheader(f"✨ {current_praise}")
    
    st.write("---")
    st.write("Tap Steve's Heart for more...")
    
    # The Heart Button to cycle phrases
    if st.button("💖", use_container_width=True):
        st.session_state.praise_index += 1
        st.rerun()
