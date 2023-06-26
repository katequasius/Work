# Created with Pyto

import streamlit as st

st.write("Hello World")


def home_page():
    streamlit run Home_Page
    
def mode1():
    st.markdown("Mode 1")
    st.sidebar.markdown("Mode 1")
    
def mode2():
    st.markdown("Mode 2")
    st.sidebar.markdown("Mode 2")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Home", "Mode 1", "Mode 2")
)
if add_selectbox = 'Mode 1':
    mode1()
elif add_selectbox = 'Mode 2':
    mode2()
else:
    home_page()
