import streamlit as st
import home
import prediction

st.set_page_config(
    page_title="Plant Diseases Detection",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/rifkyaliffa/",
        "Report a bug": "https://github.com/Penzragon",
        "About": "### Simple Plant Diseases Detection App - Kelompok 2",
    },
)

PAGES = {"Home": home, "Prediction": prediction}

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", list(PAGES.keys()))

page = PAGES[page]
page.app()
