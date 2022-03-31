import streamlit as st
import tomato
import corn
import potato


def app():
    st.markdown(
        "<h1 style='text-align: center;'>Plant Diseases Detection</h1>",
        unsafe_allow_html=True,
    )

    PLANT = {"Tomato🍅": tomato, "Corn🌽": corn, "Potato🥔": potato}

    st.sidebar.title("Plant")
    plant = st.sidebar.selectbox("Choose a plant", list(PLANT.keys()))

    plant = PLANT[plant]
    plant.app()
