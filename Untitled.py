# Created with Pyto

import streamlit as st
import Mode2Page.py as m2

st.write("Hello World")


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
	"Home": m2,
    "Mode 1": m2,
    "Mode 2": m2,
    }

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    page_names_to_funcs.keys()
)
