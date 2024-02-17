import streamlit as st
from main import session_state, db
from datetime import datetime

def create_found_item(category, description, found_at, image_url, found_date, found_by):
    found_items = db.collection('found_items').document()
    found_items.set({
        "category": category,
        "description": description,
        "found_at": found_at,
        "image_url": image_url,
        "found_date":found_date.strftime('%Y/%m/%d'),
        "found_by": found_by,
        "created_at": datetime.now().strftime('%Y/%m/%d')
    })


def report_found_item_page():
    st.title("Report Found Item")

    # Form inputs
    category = st.selectbox("Category", ["Laptop", "Phone", "Bag", "Other"])
    description = st.text_area("Description")
    image_url = st.file_uploader("Upload Image", type=["jpg", "png"])
    found_at = st.text_area("Found At:")
    found_date = st.date_input("Select a Date")
    found_by = session_state.user_data['uid']
    # Submit button
    if st.button("Submit"):
        create_found_item(category, description, found_at, image_url,found_date, found_by)
        st.success("Item reported successfully!")
        st.balloons()

if session_state.user_data:
    report_found_item_page()
else:
    st.switch_page('pages/login.py')
