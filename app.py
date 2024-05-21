

import streamlit as st
from login import login
from register import register
from upload import upload
from home import home
from about_us import about_us
from weed_details import weed_details
from user_profile import profile

st.set_page_config(layout="wide")

def main():
    st.title('🌱 Weed Detection')
    menu = st.sidebar.selectbox('Menu', ['Home', 'Profile', 'About Us', 'Upload', 'Weed Details', 'Login', 'Register'])

    if menu == 'Home':
        home()

    elif menu == 'About Us':
        about_us()

    elif menu == 'Upload':
        upload()

    elif menu == 'Weed Details':
        weed_details()

    elif  menu == 'Profile':
        username = st.session_state.get('username')
        if username:
            profile(username)
        else:
            st.write("Please login to view your profile")

    elif menu == 'Login':
        login()

    elif menu == 'Register':
        register()

if __name__ == '__main__':
    main()
