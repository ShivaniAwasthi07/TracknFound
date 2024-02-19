import streamlit as st
from main import db,bucket
from datetime import datetime

def upload_image_to_storage(image_file):
    # Upload image to Firebase Cloud Storage
    blob = bucket.blob("images/" + image_file.name)
    blob.upload_from_file(image_file)
    blob.make_public()
    # Get public URL of the uploaded image
    url = blob.public_url

    return url

def create_found_item(category, description, found_at, image_file, found_date, found_by):
    image_url = upload_image_to_storage(image_file)
    found_items = db.collection('found_items').document()
    found_items.set({
        "category": category,
        "description": description,
        "found_at": found_at,
        "image_url": image_url,
        "found_date":found_date.strftime('%Y/%m/%d'),
        "found_by": st.session_state.user_data['uid'],
        "created_at": datetime.now().strftime('%Y/%m/%d')
        # "reported_by": st.session_state.user_data['uid']
    })


def report_found_item_page():
    st.title("Report Found Item")

    # Form inputs
    category = st.selectbox("Category", ["Laptop", "Phone", "Bag", "Other"])
    description = st.text_area("Description")
    image_file = st.file_uploader("Upload Image", type=["jpg", "png"])
    found_at = st.text_area("Found At:")
    found_date = st.date_input("Found Date")
    found_by = st.session_state.user_data['uid']
    # Submit button
    if st.button("Submit"):
        create_found_item(category, description, found_at, image_file,found_date, found_by)
        st.success("Item reported successfully!")
        st.balloons()

if __name__ == "__main__":
    if 'user_data' in st.session_state:
        report_found_item_page()
    else:
        st.switch_page('pages/login.py')
