import streamlit as st
from streamApp import main
from about_page import about_page


def mainFunction():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('', ['About App', 'Prediction Page'])

    if page == 'About App':
        about_page()

    elif page == 'Prediction Page':
        main()


if __name__ == '__main__':
    try:
        mainFunction()
    except Exception as e:
        st.write("Error: ", e)
