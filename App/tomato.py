import streamlit as st
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
from io import BytesIO


def app():
    st.markdown(
        "<h1 style='text-align: center;'>🍅 Tomato 🍅</h1>",
        unsafe_allow_html=True,
    )

    img = None

    def load_prep(image):
        img = np.array(image)
        img = tf.image.resize(img, (224, 224)) / 255.0
        pred = corn_model.predict(np.expand_dims(img, axis=0))
        return pred

    corn_model = tf.keras.models.load_model("tomato_model.h5")
    class_name = [
        "Bacterial Spot",
        "Early Blight",
        "Late Blight",
        "Leaf Mold",
        "Septoria Leaf Spot",
        "Spider Mites",
        "Target Spot",
        "Yellow Leaf Curl Virus",
        "Tomato Mosaic Virus",
        "Healthy",
    ]

    options = st.selectbox("Upload an image", ("Upload", "URL"))

    if options == "Upload":
        file = st.file_uploader("Upload an image...", type=["jpg"])
        if file is not None:
            img = Image.open(file)
    else:
        url = st.text_input("Paste the URL here:")
        if url:
            try:
                response = requests.get(url)
                img = Image.open(BytesIO(response.content))
            except:
                st.error("Invalid URL, please use a different URL.")

    if img is not None:
        button = st.button("Predict")
        pred = load_prep(img)
        if button:
            st.markdown(
                "<h1 style='text-align: center;'>The predicted result is:</h1>",
                unsafe_allow_html=True,
            )
            result = f"<h3 style='text-align: center;'>{class_name[np.argmax(pred)]} ({np.max(pred)*100:.2f}% Confidence)</h3>"
            st.markdown(result, unsafe_allow_html=True)
            st.image(img, use_column_width=True)
