import streamlit as st
from PIL import Image
import tomato
import corn
import potato


def app():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        logo = Image.open("logo.png")
        st.image(logo, width=300, use_column_width=True)

    st.markdown(
        "<h4 style='text-align: center;'>🩺 Apakah Tumbuhanmu Sehat? 🌱</h4>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center;'>Aplikasi untuk mendeteksi kesehatan tumbuhan berdasarkan kondisi daun.</p>",
        unsafe_allow_html=True,
    )

    PLANT = {"Tomat🍅": tomato, "Jagung🌽": corn, "Kentang🥔": potato}

    st.sidebar.title("Plant")
    plant = st.sidebar.selectbox("Choose a plant", list(PLANT.keys()))

    plant = PLANT[plant]
    plant.app()
