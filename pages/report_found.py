import streamlit as st

def report_found_item_page():
    st.title("Report Found Item")

    # Form inputs
    category = st.selectbox("Category", ["Laptop", "Phone", "Bag", "Other"])
    description = st.text_area("Description")
    image = st.file_uploader("Upload Image", type=["jpg", "png"])

    # Submit button
    if st.button("Submit"):
        # Process the submitted data (e.g., save to database)
        st.success("Item reported successfully!")
        st.balloons()

# Display the report found item page
report_found_item_page()