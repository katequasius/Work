# Created with Pyto

import streamlit as st

st.write("Hello World")
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    page_names_to_funcs.keys()
)

def home_page():
    st.markdown("Home")
    st.sidebar.markdown("Home")
    
def mode1():
    st.markdown("Mode 1")
    st.sidebar.markdown("Mode 1")
    
def mode2():
    st.markdown("Mode 2")
    st.sidebar.markdown("Mode 2")
    
page_names_to_funcs = {
	"Home": Mode2Page,
    "Mode 1": Mode2Page,
    "Mode 2": Mode2Page,
    }

