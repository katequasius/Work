# Created with Pyto

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Investor Reachout")
def home_page():
    st.header("Home Page")
    st.write("Mode 1: Select if you have the name and phone number of the investor")
    st.write("Mode 2: Select if you have the name, phone number, and desired location of the investor")
    image = Image.open('ProgressLogo.PNG')
    st.image(image, caption=None, width=2, use_column_width=True)
    
def mode1():
    st.header("Mode 1")
    st.write("Select if you have the name and phone number of the investor")
    investor = st.text_input('Investor Name')
    number = st.text_input('Investor Phone Number')
    sourcer = st.text_input('Sourcer Name')
    text = "https://wa.me/" + number + "?text=Hello%20" + investor + ",%0A%0ANice%20to%20be%20in%20contact,%20I'm%20from%20Progress%20Property,%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%20%0A%0AI%20look%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcer + "%0AProgress%20Property%20Services%20Ltd%0Ahttps://progresspropertyservices.co"
    if st.button('Submit'):
        if checkNumber(number) == 1:
            st.write("Invalid number. Do not include spaces or special characters.")
        else:
            st.write(text)
    
def mode2():
    st.header("Mode 2")
    st.write("Select if you have the name, phone number, and desired location of the investor")
    investor = st.text_input('Investor Name')
    number = st.text_input('Investor Phone Number')
    location = st.text_input('Desired Location')
    sourcer = st.text_input('Sourcer Name')
    text = "https://wa.me/" + number + "?text=Hello%20" + investor + ",%0A%0ANice%20to%20be%20in%20contact,%20I'm%20from%20Progress%20Property,%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%20From%20our%20previous%20contact,%20we%20see%20that%20you're%20interested%20in%20the%20"+location+"%20area.%20%0A%0AI%20look%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcer + "%0AProgress%20Property%20Services%20Ltd%0Ahttps://progresspropertyservices.co"
    if st.button('Submit'):
        st.write(text)

def checkNumber(num):
    check = 0
    for i in range(0, len(num)):
        if num.charAt(i) < 48 or num.charAt(i) > 57:
            check = 1
    return check
        

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
