# # about_us.py

# import streamlit as st

# def about_us():
#     st.write('### About Us')
#     st.write("Empowering growers with cutting-edge weed detection technology for healthier crops and sustainable agriculture")

import streamlit as st

def about_us():
    st.markdown(
        """
        <style>
            /* Add some padding to the page */
            body {
                padding: 20px;
                background-color: #000000; /* Set the background color to black */
                color: #ffffff; /* Set text color to white */
            }
           
            /* Style the h1 heading */
            h1 {
                font-size: 36px;
                font-weight: bold;
                color: #ffffff; /* Set heading color to white */
                margin-bottom: 20px;
            }
            /* Style the paragraph */
            p {
                font-size: 18px;
                color: #ffffff; /* Set paragraph color to white */
                margin-bottom: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.write('<div class="main-container">', unsafe_allow_html=True)
    st.write('<h1>About Us</h1>', unsafe_allow_html=True)
    st.write('<p>Empowering growers with cutting-edge weed detection technology for healthier crops and sustainable agriculture.</p>', unsafe_allow_html=True)
    st.write('</div>', unsafe_allow_html=True)
