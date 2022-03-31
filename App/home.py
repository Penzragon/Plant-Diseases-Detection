import streamlit as st


def app():
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            "<h1 style='text-align: center;'>🏠 Home 🏠</h1>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align: center;'>This simple app is a computer vision project for detecting a forest fire using <strong>Convolutional Neural Network</strong>, you can see the dataset used in this project on <a href='https://www.kaggle.com/datasets/phylake1337/fire-dataset'>Kaggle</a>.</p>",
            unsafe_allow_html=True,
        )

        with st.expander("Please Open🔓"):
            st.write(
                "<b>The app is far from optimized</b>. If you find any issue or have any suggestion, you can report it on the <a href='https://github.com/Penzragon'>GitHub repository</a> or contact me on <a href='https://www.linkedin.com/in/rifkyaliffa/'>LinkedIn</a>. Thank you!",
                unsafe_allow_html=True,
            )

        with st.expander("DO NOT OPEN!⛔"):
            st.markdown(
                "<h3 style='text-align: center;'>Aaaaaa!</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<img src='https://media.giphy.com/media/nrXif9YExO9EI/giphy.gif' width='100%'/>",
                unsafe_allow_html=True,
            )
        st.markdown(
            "<p style='text-align: center;'>Made with <span style='color: red'>♥️</span> by <b>Rifky Aliffa</b></p>",
            unsafe_allow_html=True,
        )
