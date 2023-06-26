# Created with Pyto

import streamlit as st

st.write("Hello World")
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Home", "Mode 1", "Mode 2")
)
