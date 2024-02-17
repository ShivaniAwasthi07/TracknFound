import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from main import create_user # This line brings all environment variables from .env into os.environ
from main import session_state





def login_function(email, password):
    try:
        user = auth.get_user_by_email(email)
        # print(user)
        # print(user.uid)
        session_state.user_data = {
            "uid": user.uid,
            "email": user.email,
            "display_name": user.display_name
        }
        st.success("Login successful!")
        st.switch_page('pages/home.py')

    except Exception as e:
        print(e)
        st.warning('Login failed')


def create_account():
    st.subheader("Create Account")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Implement code to save user data to database
    if st.button("Create Account"):
        user=auth.create_user(email=email,password=password,id=username)
        st.success("Account created successfully!")
        st.balloons()
        create_user(username, email)
        st.rerun()
        
        

# Define function for user login
def login():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Implement code to authenticate user
    if st.button("Login"):
        login_function(email,password)
    
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
