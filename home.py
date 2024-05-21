 # home.py

import streamlit as st


def home():
    st.write('### Home')
    st.image("https://wallpapercave.com/wp/wp6139408.jpg", width=600)

    if getattr(st.session_state, 'logged_in', False):
        st.write(f"Logged in as: {st.session_state.username}")
        st.write("User profile information here")
        st.write("Options for weed details or image upload")
    else:
       st.write("Please login to view your profile.")
       

