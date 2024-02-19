import firebase_admin
from firebase_admin import firestore,credentials,auth,storage
import streamlit as st
from dotenv import load_dotenv
import os
from datetime import datetime

# Initializing a session state
# class SessionState:
#     def __init__(self):
#         self.user_data = None

def create_user_db(username, email):
    user_ref = db.collection('users').document()
    user_ref.set({
        'username': username,
        'email': email
    })

# Create session state object
# session_state = SessionState()
# session_state.user_data = None


load_dotenv()

if not firebase_admin._apps:
    cred_json = {
        'type': os.environ['TYPE'],
        'project_id': os.environ['PROJECT_ID'],
        "private_key_id": os.environ['PRIVATE_KEY_ID'],
        "private_key": os.environ['PRIVATE_KEY'],
        "client_email": os.environ['CLIENT_EMAIL'],
        "client_id": os.environ['CLIENT_ID'],
        "auth_uri": os.environ['AUTH_URI'],
        "token_uri": os.environ['TOKEN_URI'],
        "auth_provider_x509_cert_url": os.environ['AUTH_PROVIDER_X509_CERT_URL'],
        "client_x509_cert_url":os.environ['CLIENT_X509_CERT_URL'],
        "universe_domain": os.environ['UNIVERSE_DOMAIN']
    }
    cred=credentials.Certificate(cred_json)
    firebase_admin.initialize_app(cred, {
    'storageBucket': 'tracknfound.appspot.com'
})
db = firestore.client()
bucket = storage.bucket()


# if session_state.user_data:
#     st.switch_page('pages/home.py')
# else:
#     st.switch_page('pages/login.py')


def clickable_card(title, page):
    st.markdown(
        """
        <style>
        .element-container:has(style){
            display: none;
        }
        #button-after {
            display: none;
        }
        .element-container:has(#button-after) {
            display: none;
        }
        .element-container:has(#button-after) + div button {
            background-color: #006193;
            padding: 4rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s ease;
            width: 350px;
            height: 250px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 24px;
            color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)

    if st.button(title):
        st.switch_page(f'pages/{page}')


# Create clickable cards in each column based on the grid layout
if 'user_data' in st.session_state: 
    # Page starts
    st.set_page_config(layout="centered")
    st.title("Digital Lost and Found Platform")


    # Create a two-dimensional array for the grid layout
    grid_layout = [
        [0, 1],
        [2, 3]
    ]

    # Create layout using Streamlit columns
    col1, col2 = st.columns(2)  
    for row in grid_layout:
        for box_num in row:
            if box_num == 0:
                with col1:
                    clickable_card('Report Found', 'report_found.py')
            elif box_num == 1:
                with col1:
                    clickable_card('Report Lost', 'report_lost.py')
            elif box_num == 2:
                with col2:
                    clickable_card('Browse Lost', 'browse_lost.py')
                    
            elif box_num == 3:
                with col2:
                    clickable_card('Browse Found', 'browse_found.py')
else:
    st.write("Seems like you are not logged in")
    if st.button("Click here to login"):
        st.switch_page("pages/login.py")