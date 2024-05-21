import streamlit as st
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["weed_detector"]
collection = db["users"]

def get_user_details(username):
    user = collection.find_one({"username": username}, {"_id": 0, "email": 1, "mobile": 1})
    return user if user else None

def profile(username):
    st.write('### Profile')
    user_details = get_user_details(username)

    if user_details:
        st.write(f"Username: {username}")
        st.write(f"Email: {user_details['email']}")
        st.write(f"Mobile: {user_details['mobile']}")
    else:
        st.write("User details not found.")

