import streamlit as st
import random as r

# Set page configuration
st.set_page_config(
    page_title="First Py App",
    page_icon="img.png",
    layout="wide"
)

st.markdown(
    """
    <h1>issa ghnaim</h1>
    <style>
    .stApp {
        background-color: blue;  /* Light gray background */
    }
    </style>
    """,
    unsafe_allow_html=True
)


if "ans" not in st.session_state:
    st.session_state["ans"] = r.randint(1,100);

if "guess" not in st.session_state:
    st.session_state["guess"] = 1;


 
guess = st.number_input('selsect number from 1 to 100',min_value=1,max_value=100)

if guess > st.session_state["ans"]:
    st.title('lower')
elif guess < st.session_state["ans"]:
    st.title('higher')
else:
    st.title('correct')

    if st.button('reset'):
         st.session_state['ans'] = r.randint(1, 100)
         st.session_state["guess"] = 1
         st.rerun()