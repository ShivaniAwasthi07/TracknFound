import streamlit as st
from main import session_state, db,bucket
from datetime import datetime

def upload_image_to_storage(image_file):
    # Upload image to Firebase Cloud Storage
    blob = bucket.blob("images/" + image_file.name)
    blob.upload_from_file(image_file)
    blob.make_public()
    # Get public URL of the uploaded image
    url = blob.public_url

    return url

def create_lost_item(category, description, last_seen, image_file, lost_date, owner):
    image_url = upload_image_to_storage(image_file)
    found_items = db.collection('lost_items').document()
    found_items.set({
        "category": category,
        "description": description,
        "last_seen": last_seen,
        "image_url": image_url,
        "lost_date":lost_date.strftime('%Y/%m/%d'),
        "owner": owner,
        "created_at": datetime.now().strftime('%Y/%m/%d'),
        "reported_by": session_state.user_data['uid']
    })


def report_lost_item_page():
    st.title("Report Found Item")

    # Form inputs
    category = st.selectbox("Category", ["Laptop", "Phone", "Bag", "Other"], key='category')
    description = st.text_area("Description")
    image_file = st.file_uploader("Upload Item Image", type=["jpg", "png"])
    last_seen = st.text_area("Last Seen:")
    lost_date = st.date_input("Lost Date")
    owner = session_state.user_data['uid']
    # Submit button
    if st.button("Submit"):
        create_lost_item(category, description, last_seen, image_file,lost_date, owner)
        st.success("Item reported successfully!")
        st.balloons()

if session_state.user_data:
    report_lost_item_page()
else:
    st.switch_page('pages/login.py')
