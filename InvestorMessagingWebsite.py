
import streamlit as st
import webbrowser
from PIL import Image

#Home page setup
st.set_page_config(page_title="Investor Reachout")
def checkNumber(num):
    check = 0
    for i in num:
        if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            check += 1
    if check != len(num):
        return True
    else: 
        return False
        
#Replaces space character with a '%20' to make the text work for the URL
def checkSpaces(str):
    new = ""
    for i in str:
        if i == ' ':
            new = new + '%20'
        else:
            new = new + i
    return new
    
def home_page():
    st.title("Investor Contact Form")
    st.write("Fields marked with a * are required")
    investor = checkSpaces(st.text_input('Investor Name *'))
    col1, col2 = st.columns([0.42, 1.58])
    with col1:
        countryCode = st.text_input('Investor Country Code *')
    with col2:
        number = st.text_input('Investor Phone Number * *(No spaces or special characters)*')
    location = checkSpaces(st.text_input('Desired Location'))
    sourcer = checkSpaces(st.text_input('Sourcer Name *'))
    #Error Checking
    if st.button('Click to generate WhatsApp Message'):
        if countryCode == "":
            st.write("Error. Need to include a country code.")
        elif checkNumber(number):
            st.write("Invalid number. Do not include spaces or special characters in phone number.")
        elif checkNumber(countryCode):
            st.write("Invalid number. Do not include spaces or special characters in country code.")
        else:
            if location != "":
                st.write("WhatsApp Message [Link](https://wa.me/" + countryCode + number + "?text=Hello%20" + investor + ",%0A%0ANice%20to%20be%20in%20contact,%20I'm%20from%20Progress%20Property,%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%20From%20our%20previous%20contact,%20we%20see%20that%20you're%20interested%20in%20the%20"+location+"%20area.%20%0A%0AI%20look%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcer + "%0AProgress%20Property%20Services%20Ltd%0Ahttps://progresspropertyservices.co)")
            else:
                message = st.selectbox("Choose message", ("Message 1", "Message 2", "Message 3"))
                if message == "Message 1":
                    st.write("WhatsApp Message [Link](https://wa.me/" + countryCode + number + "?text=Hello%20" + investor + ",%0A%0ANice%20to%20be%20in%20contact,%20I'm%20from%20Progress%20Property,%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%20%0A%0AI%20look%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcer + "%0AProgress%20Property%20Services%20Ltd%0Ahttps://progresspropertyservices.co)")
                    st.write("**Message 1**  \nHello [Investor Name],  \nNice to be in contact, I'm from Progress Property, we find HMO properties for company let on behalf of our clients helping them grow their portfolios.  \n\nWe have been in contact with you before and we're interested in seeing what new business we can do!  \n\n Look forward to hearing back from you. Thanks.  \n\n[Sourcer Name]  \nProgress Property Services Ltd  \nprogresspropertyservices.co")
                elif message == "Message 2":
                    st.write("WhatsApp Message [Link](https://wa.me/" + countryCode + number + "?text=Hello,%20"+investor+"%0ANice%20to%20be%20in%20contact.%0A%0AI'm%20representing%20Progress%20Property%20Services%20Ltd%20-%20specialists%20in%20finding%20high%20yielding%20company%20let%20opportunities.%0A%0AWe%20came%20across%20your%20company%20and%20we%20are%20interested%20in%20what%20business%20we%20can%20do!%0A%0AI%20look%20forward%20to%20hearing%20from%20you.%20Thanks,%0A%0A"+sourcer+"%20|%20Business%20Development%20Consultant%0AProgress%20Property%20Services%20Ltd%0Ahttps://progresspropertyservices.co")
                    st.write("**Message 2**  \nHello, [Investor Name]  \nNice to be in contact.  \n\nI'm representing Progress Property Services Ltd - specialists in finding high yielding company let opportunities.  \n\nWe came across your company and we are interested in what business we can do!  \n\nI look forward to hearing from you. Thanks,  \n\n[Sourcer Name] | Business Development Consultant  \nProgress Property Services Ltd  \nprogresspropertyservices.co")
                else:
                    st.write("")
                    st.write("**Message 3**  \nHello [Investor Name],  \nI'm from Progress Property. We assist management companies in London. A lot of our clients are companies who are looking to house working professionals, social housing providers, letting agents...etc.  \n\nWe started doing business three years ago and have seen good results and are looking to invest more money into our property finding efforts in order to ensure that there are very few 'fit-for-purpose' properties in the UK that go overlooked.  \n\nCan you give me a similar scope for what you do? Do you deal with other companies similar to ourselves or are you a lettings company yourself?  \n\nWill this be our best contact for us to send you our latest deals?  \n\nThanks,  \n[Sourcer Name]  \nProgress Property Services Ltd  \nprogresspropertyservices.")
                
home_page()

#Mode 1 setup
# def mode1():
#     st.header("Mode 1")
#     st.write("Fields marked with a * are required")
#     investor = checkSpaces(st.text_input('Investor Name'))
#     col1, col2 = st.columns([0.4, 1.6])
#     with col1:
#         countryCode = st.text_input('Investor Country Code')
#     with col2:
#         number = st.text_input('Investor Phone Number *(No spaces or special characters)*')
#     location = checkSpaces(st.text_input('Desired Location'))
#     sourcer = checkSpaces(st.text_input('Sourcer Name'))
#     #Error Checking
#     if st.button('Click to generate WhatsApp Message'):
#         if countryCode == "":
#             st.write("Error. Need to include a country code.")
#         elif checkNumber(number):
#             st.write("Invalid number. Do not include spaces or special characters in phone number.")
#         elif checkNumber(countryCode):
#             st.write("Invalid number. Do not include spaces or special characters in country code.")
#         else:
#             if location != "":
#                 st.write("WhatsApp Message [Link](https://wa.me/" + countryCode + number + "?text=Hello%20" + investor + ",%0A%0ANice%20to%20be%20in%20contact,%20I'm%20from%20Progress%20Property,%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%20From%20our%20previous%20contact,%20we%20see%20that%20you're%20interested%20in%20the%20"+location+"%20area.%20%0A%0AI%20look%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcer + "%0AProgress%20Property%20Services%20Ltd%0Ahttps://progresspropertyservices.co)")
#             else:
#                 st.write("WhatsApp Message [Link](https://wa.me/" + countryCode + number + "?text=Hello%20" + investor + ",%0A%0ANice%20to%20be%20in%20contact,%20I'm%20from%20Progress%20Property,%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%20%0A%0AI%20look%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcer + "%0AProgress%20Property%20Services%20Ltd%0Ahttps://progresspropertyservices.co)")

#Mode 2 setup
# def mode2():
#     st.header("Mode 2")
#     st.write("Use if you have the **name**, **phone number**, and **desired location** of the investor.")
#     investor = checkSpaces(st.text_input('Investor Name'))
#     col1, col2 = st.columns([0.4, 1.6])
#     with col1:
#         countryCode = st.text_input('Investor Country Code')
#     with col2:
#         number = st.text_input('Investor Phone Number *(No spaces or special characters)*')
#     location = checkSpaces(st.text_input('Desired Location'))
#     sourcer = checkSpaces(st.text_input('Sourcer Name'))
#     #Error Checking
#     if st.button('Click to generate WhatsApp Message'):
#         if countryCode == "":
#             st.write("Error. Need to include a country code.")
#         elif checkNumber(number):
#             st.write("Invalid number. Do not include spaces or special characters in phone number.")
#         elif checkNumber(countryCode):
#             st.write("Invalid number. Do not include spaces or special characters in country code.")
#         elif location == "":
#             st.write("Error. Need to include one or more locations.")
#         else:
#             st.write("WhatsApp Message [Link](https://wa.me/" + countryCode + number + "?text=Hello%20" + investor + ",%0A%0ANice%20to%20be%20in%20contact,%20I'm%20from%20Progress%20Property,%20we%20find%20HMO%20properties%20for%20company%20let%20on%20behalf%20of%20our%20clients%20helping%20them%20grow%20their%20portfolios.%20%0AWe%20have%20been%20in%20contact%20with%20you%20before%20and%20we're%20interested%20in%20seeing%20what%20new%20business%20we%20can%20do!%20From%20our%20previous%20contact,%20we%20see%20that%20you're%20interested%20in%20the%20"+location+"%20area.%20%0A%0AI%20look%20forward%20to%20hearing%20back%20from%20you.%20Thanks.%20%0A%0A" + sourcer + "%0AProgress%20Property%20Services%20Ltd%0Ahttps://progresspropertyservices.co)")

#Phone number check to make sure there are no spaces or special characters

