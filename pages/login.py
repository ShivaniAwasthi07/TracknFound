import streamlit as st
from firebase_admin import auth
from main import create_user_db # This line brings all environment variables from .env into os.environ


def login_function():
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Implement code to authenticate user
    if st.button("Login"):
        try:
            user = auth.get_user_by_email(email)
            # print(user)
            # print(user.uid)
            user_dict = {
                "uid": user.uid,
                "email": user.email,
                "display_name": user.display_name
            }
            st.session_state.user_data = user_dict
            st.success("Login successful!")
            st.switch_page('main.py')

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
        user=auth.create_user(email=email,password=password)
        st.success("Account created successfully!")
        st.balloons()
        create_user_db(username, email)
        # st.rerun()
        
    
st.title("Login Page")
option = st.selectbox('Login/Sign-Up',['Login', "Sign-Up"])

if option == 'Sign-Up':
    create_account()
    # create_account_option = 'Login'
    # st.switch_page('pages/login.py')
else:
    login_function()


# if st.button("Sign In"):
#     st.switch_page('pages/home_page.py')
