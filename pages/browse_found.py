import streamlit as st
from datetime import date
from main import session_state


def browse_found_item_page():
    st.title("Browse Found Item")

    category = st.selectbox("category",["Laptop","Phone","Bag","Other"])
    date = st.date_input("Select the date")
    lastseen = st.text_input("Found location")
    description = st.text_area("Description")
    image = st.file_uploader("Upload Image", type=["jpg", "png"])

    if st.button("Submit"):
        # Process the submitted data (e.g., save to database)
        st.success("Item reported successfully!")
        st.balloons()

# Display the report found item page

if session_state.user_data:
    browse_found_item_page()
else:
    st.switch_page('pages/login.py')