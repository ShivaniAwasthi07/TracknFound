import streamlit as st
from main import session_state, db

# Function to fetch found items from Firebase Firestore
def fetch_found_items():
    found_items_ref = db.collection('found_items')
    found_items = found_items_ref.get()
    return found_items

# Main function to display found items
def browse_found_items():
    st.title("Browse Found Items")
    
    # Fetch found items from Firestore
    found_items = fetch_found_items()
    
    # Display found items in a table
    if found_items:
        data = []
        for item in found_items:
            item_data = item.to_dict()
            data.append(item_data)
        
    else:
        st.write("No items found.")

# Display the report found item page

if session_state.user_data:
    browse_found_items()
else:
    st.error("Please log in to browse found items.")
    st.button("Log In")

