# run file in VSCode
# streamlit run app.py

import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import streamlit_calendar as stcal
from streamlit_option_menu import option_menu
    
with open("./admin.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Check if image hiding state exists in session state, if not, initialize it
if "image_hiding_state" not in st.session_state:
    st.session_state.image_hiding_state = {
        "chbox1": False,
        "chbox2": False,
        "chbox3": False,
        "chbox4": False
    }

if "cal" not in st.session_state:
    st.session_state["cal"] = stcal.calendar()


with st.sidebar:
    choice = option_menu("Anika's Demo Site",
                        ['Home', 'About', 'Upcoming Events'],
                        icons = ['house-fill', 'stars', 'calendar-fill'],
                        menu_icon="moon-stars-fill", default_index=0,
                        styles={
                            # Area the menu lives in
                            "container": {"padding": "5!important", "background-color": "#8FC0A9"},
                            # Design notes for icons
                            "icon": {"color": "#B15E6C", "font-size": "25px"}, 
                            # New page
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#EEC643"},
                            # Current page
                            "nav-link-selected": {"background-color": "#12664F"},
    })

name, authentication_status, username = authenticator.login('Admin Login', 'sidebar')
if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.header(f'Welcome, {name}!')
    st.subheader('This page has been updated to Admin Mode.')
elif authentication_status == False:
    st.error('Username/password is incorrect')

if choice == "Home":

    with st.columns(3)[1]:
        st.image('Images/brand-img.jpg')

    st.title('Hello, world!', )
    st.header('This page is for introducing your website, product, and ideas!')
    st.subheader('These images are relevant and cool :)')
    
    col1, col2 = st.columns(2, gap="small")

    with col1:

        one = st.image("https://images.unsplash.com/photo-1606841613102-2bfd25e23265?q=80&w=700")
        two = st.image("https://images.unsplash.com/photo-1534531173927-aeb928d54385?q=80&w=800")

        if st.session_state.image_hiding_state["chbox1"]:
            one.empty()
        if st.session_state.image_hiding_state["chbox2"]:
            two.empty()
        
        if authentication_status:
            st.session_state.image_hiding_state["chbox1"] = st.checkbox("Hide image 1?", key="chbox1", value=st.session_state.image_hiding_state["chbox1"])
            st.session_state.image_hiding_state["chbox2"] = st.checkbox("Hide image 2?", key="chbox2", value=st.session_state.image_hiding_state["chbox2"])

    with col2:
        three = st.image("https://images.unsplash.com/photo-1517410634401-2eba0798f97b?q=80&w=700")
        four = st.image("https://images.unsplash.com/photo-1528754704377-60e053a66165?q=80&w=700")

        if st.session_state.image_hiding_state["chbox3"]:
            three.empty()
        if st.session_state.image_hiding_state["chbox4"]:
            four.empty()

        if authentication_status:
            st.session_state.image_hiding_state["chbox3"] = st.checkbox("Hide image 3?", key="chbox3", value=st.session_state.image_hiding_state["chbox3"])
            st.session_state.image_hiding_state["chbox4"] = st.checkbox("Hide image 4?", key="chbox4", value=st.session_state.image_hiding_state["chbox4"])

elif choice == "About":
    st.subheader("Some basic facts about what we do!")
    st.balloons()

elif choice=="Upcoming Events":

    st.header("When to find us!")

    calendar_options = {"selectable": True}
    
    calendar_events = [
    {
        "title": "Streamlit Presentation",
        "start": "2024-06-06T13:00:00",
        "end": "2024-06-06T14:00:00",
        "resourceId": "a",
    },
    {
        "title": "Day of Code",
        "start": "2024-06-10",
        "end": "2024-06-10",
        "resourceId": "b",
    },
    {
        "title": "D&D",
        "start": "2024-06-06T18:00:00",
        "end": "2024-06-06T20:00:00",
        "resourceId": "a",
    }
    ]

    stcal.calendar(options=calendar_options, events=calendar_events, key="cal")
    if "eventClick" not in st.session_state.cal:
        st.subheader("Choose an event for details")
    else:
        event = st.session_state["cal"]["eventClick"]["event"]
        st.subheader(event["title"])
        if event["allDay"]:
            st.subheader("All Day Event")
        else:
            st.subheader(f'Start: {event["start"]}')
            st.subheader(f'End: {event["end"]}')       
