# Created with Pyto

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Investor Reachout")
def home_page():
    st.header("Home Page")
    st.write("Mode 1: Select if you have the name and phone number of the investor")
    st.write("Mode 2: Select if you have the name, phone number, and desired location of the investor")
    image = Image.open('ProgressLogo.PNG')
    st.image(image, caption=None, width=5, use_column_width=True)
    
def mode1():
    st.header("Mode 1")
    st.write("Select if you have the name and phone number of the investor")
    st.text_input('Investor Name')
    st.text_input('Investor Phone Number')
    st.text_input('Sourcer Name')
    
def mode2():
    st.header("Mode 2")
    st.write("Select if you have the name, phone number, and desired location of the investor")
    st.text_input('Investor Name')
    st.text_input('Investor Phone Number')
    st.text_input('Desired Location')
    st.text_input('Sourcer Name')

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
