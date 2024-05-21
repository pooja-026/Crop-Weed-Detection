# register.py

import streamlit as st
import pymongo
from werkzeug.security import generate_password_hash

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["weed"]
collection = db["crop_users"]

def register():
    st.write('### Register')
    new_username = st.text_input('New Username')
    new_password = st.text_input('New Password', type='password')
    confirm_password = st.text_input('Confirm Password', type='password')
    email = st.text_input('Email')
    mobile = st.text_input('Mobile Number')
    
    if new_password != confirm_password:
        st.error('Passwords do not match. Please try again.')
    elif st.button('Register'):
        if create_user(new_username, new_password, email, mobile):
            st.success('Registration successful! Please login to continue.')
        else:
            st.error('Username already exists. Please choose a different username.')

def create_user(username, password, email, mobile):
    # Check if username already exists
    if collection.find_one({"username": username}):
        return False
    
    # Hash the password before storing it
    hashed_password = generate_password_hash(password)
    
    # Insert the new user into the users collection
    user_data = {
        "username": username,
        "password": hashed_password,
        "email": email,
        "mobile": mobile
    }
    collection.insert_one(user_data)
    
    return True
