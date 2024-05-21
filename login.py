# login.py

import streamlit as st
import pymongo
from werkzeug.security import check_password_hash

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["weed"]
collection = db["crop_users"]

def login():
    st.write('### Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if validate_login(username, password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success('Login successful!')
        else:
            st.error('Invalid username or password')

def validate_login(username, password):
    user = collection.find_one({"username": username})
    if user and check_password_hash(user["password"], password):
        return True
    return False
