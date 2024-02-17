# from dotenv import load_dotenv
# import os
# 
# def run():
#     load_dotenv()  # This line brings all environment variables from .env into os.environ
#     print(os.environ['TYPE'])
# 
# run()

# import streamlit as st
# 
# st.session_state.otp = False
# 
# st.title("Login")
# 
# # Email input
# email = st.text_input("Email")
# 
# # Button to send OTP
# 
# if st.button("Send OTP"):
#     st.session_state.otp = True
# # OTP input
# 
# # if st.session_state.otp:
# otp = st.text_input("OTP")
# 
# # Redirect to home page on sign-in



import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from main import create_user
from dotenv import load_dotenv
import os

load_dotenv()  # This line brings all environment variables from .env into os.environ




def login_function(email):
    try:
        user=auth.get_user_by_email(email)
        st.success("Login successful!")
        st.switch_page('pages/home_page.py')
    except Exception as e:
        st.warning('Login failed')
def create_account():
    st.subheader("Create Account")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Implement code to save user data to database
    if st.button("Create Account"):
        user=auth.create_user(email=email,password=password,uid=username)

        st.success("Account created successfully!")
        st.balloons()
        # st.text_input("Username", value="", key="clear_username_input")
        # st.text_input("Email", value="", key="clear_email_input")
        # st.text_input("Password", value="", key="clear_password_input")
        create_user(username, email)
        st.rerun()
        
        

# Define function for user login
def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Implement code to authenticate user
    if st.button("Login"):
        login_function(email)
    
def main():
    st.title("Login Page")
    create_account_option = st.selectbox('Login/Sign-Up',['Login','Sign-Up'])

    if create_account_option == 'Sign-Up':
        create_account()
        create_account_option = 'Login'
        # st.switch_page('pages/login.py')

    else:
        login()

if __name__ == "__main__":
    main()

# if st.button("Sign In"):
#     st.switch_page('pages/home_page.py')
