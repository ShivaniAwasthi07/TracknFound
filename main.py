import firebase_admin
from firebase_admin import firestore,credentials,auth,storage
import streamlit as st
from dotenv import load_dotenv
import os
from datetime import datetime

# Initializing a session state
class SessionState:
    def __init__(self):
        self.user_data = None

def create_user(username, email):
    user_ref = db.collection('users').document()
    user_ref.set({
        'username': username,
        'email': email
    })

# Create session state object
session_state = SessionState()

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

st.set_page_config(initial_sidebar_state='collapsed')

if session_state.user_data:
    st.switch_page('pages/home.py')
else:
    st.switch_page('pages/login.py')


