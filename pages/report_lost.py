import streamlit as st
from datetime import date

def report_lost_item_page():
    st.title("Report Lost Item")

    # Form inputs
    category = st.selectbox("Category", ["Laptop", "Phone", "Bag", "Other"])
    date = st.date_input("Select a Date")
    lastseen= st.text_input("Last seen location")
    description = st.text_area("Description")
    image = st.file_uploader("Upload Image", type=["jpg", "png"])

    # Submit button
    if st.button("Submit"):
        # Process the submitted data (e.g., save to database)
        st.success("Item reported successfully!")
        st.balloons()

# Display the report found item page
report_lost_item_page()