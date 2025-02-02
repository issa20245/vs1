import streamlit as st
import random as r
st.set_page_config (
    page_title='guess the number game'
)
# Function to reset the random number
def c():
    st.session_state['r'] = r.randint(1, 100)

st.title('Guess the Number Game 🎯')

# User input
num = st.number_input('Select a number:', min_value=1, max_value=100, step=1)

# Initialize random number if not set
if 'r' not in st.session_state:
    st.session_state['r'] = r.randint(1, 100)

# Game Logic
if num:
    if num == st.session_state['r']:
        st.success('🎉 You win!')
        st.button('Restart Game 🔄', on_click=c)
    elif num > st.session_state['r']:
        st.warning('⬇ Try a smaller number!')
    else:
        st.warning('⬆ Try a bigger number!')

# Set Background Color (Properly)
st.markdown(
    """
    <style>
    .stApp {
        background-color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

