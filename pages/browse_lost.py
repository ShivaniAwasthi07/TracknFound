import streamlit as st
from main import session_state, db

# Function to fetch found items from Firebase Firestore
def fetch_lost_items():
    lost_items_ref = db.collection('lost_items')
    lost_items = lost_items_ref.get()
    return lost_items

# Main function to display found items
def browse_lost_items():
    st.title("Browse Lost Items")
    
    # Fetch found items from Firestore
    lost_items = fetch_lost_items()
    
    # Display found items in a table
    if lost_items:
        data = []
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader("  Image")
        with col2:
            st.subheader("  Data")
        with col4:
            st.subheader('  Actions')
        
        
        for item in lost_items:
            item_data = item.to_dict()
            data.append(item_data)

            with st.container(  border=True):
                col1, col2, col3, col4 = st.columns(4)

            
                with col1:
                    st.image(item_data['image_url'], width=200)

                with col2:
                    temp = item_data.pop('image_url')
                    for key, value in item_data.items():
                        st.write(key, ': ', value)
                

                with col4:
                    st.header("")
                    st.header("")
                    st.header("")
                    st.button('Claim', key=item)
            
    else:
        st.write("No items found.")

# Display the report found item page    
if session_state.user_data:
    st.set_page_config(layout="wide")
    browse_lost_items()
else:
    st.switch_page('pages/login.py')
