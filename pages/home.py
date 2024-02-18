import streamlit as st
from main import session_state

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

# Create clickable cards in each column based on the grid layout
if session_state.user_data:   
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
    st.switch_page('pages/login.py')
                

