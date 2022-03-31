import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


def app():
    st.markdown(
        "<h1 style='text-align: center;'>🌽 Corn 🌽</h1>",
        unsafe_allow_html=True,
    )

    def load_prep(image):
        img = np.array(image)
        img = tf.image.resize(img, (150, 150)) / 255.0
        pred = corn_model.predict(np.expand_dims(img, axis=0))
        return pred

    corn_model = tf.keras.models.load_model("mobilenetmodel.h5")
    class_name = ["Gray Leaf Spot", "Common Rust", "Northern Leaf Blight", "Healthy"]

    img = st.file_uploader("Upload an image...", type=["jpg"])
    if img:
        button = st.button("Predict")
        if button:
            st.image(img, use_column_width=True)
            img = Image.open(img)
            pred = load_prep(img)
            st.title(class_name[np.argmax(pred)])
            st.title(f"{np.max(pred)*100:.2f}%")