import streamlit as st
from main import db

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
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader("  Image")
        with col2:
            st.subheader("  Data")
        with col4:
            st.subheader('  Actions')
        
        
        for item in found_items:
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
                    if st.session_state.user_data['uid'] == item_data["found_by"]:
                        st.button('Delete', key=item)
                    else:
                        st.button('Claim', key=item)
                                    
    else:
        st.write("No items found.")
if __name__ == "__main__":
    # Display the report found item page    
    if 'user_data' in st.session_state:
        st.set_page_config(layout="wide")
        browse_found_items()
    else:
        st.switch_page('pages/login.py')

