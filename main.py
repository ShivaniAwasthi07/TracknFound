import streamlit as st
from firebase_admin import firestore,credentials,auth,storage
import firebase_admin
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
        'email': email,
    })

def create_lost_item(category, description, last_seen, image_url, found_by):
    lost_items_ref = db.collection('lost_items').document()
    lost_items_ref.set({
        "category": category,
        "description": description,
        "last_seen": last_seen,
        "image_url": image_url,
        "lost_date":lost_date,
        "found_by": found_by,
        "created_at": datetime.now()
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


