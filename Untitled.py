# Created with Pyto

import streamlit as st



def home_page():
    st.write("This is home page")
    st.header("Home Page")
    
def mode1():
    st.write("This is Mode 1")
    
def mode2():
    st.write("This is Mode 2")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Home", "Mode 1", "Mode 2")
)
if add_selectbox == 'Mode 1':
    mode1()
elif add_selectbox == 'Mode 2':
    mode2()
else:
    home_page()
