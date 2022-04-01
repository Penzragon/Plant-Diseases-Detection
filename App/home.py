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

        with st.expander("About Us"):
            st.markdown(
                "<h3 style='text-align: center;'>Kevin Giovanni Pradana</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align: center;'><a href='https://www.linkedin.com/in/kevin-giovanni-pradana-50aa61145/'>Linkedin</a></p>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align: center;'><a href='https://github.com/KevinGiovanniP'>GitHub</a></p>",
                unsafe_allow_html=True,
            )

            st.markdown("<hr>", unsafe_allow_html=True)

            st.markdown(
                "<h3 style='text-align: center;'>Muhammad Bintang Ramadhan</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align: center;'><a href='https://www.linkedin.com/in/muhammad-bintang-ramadhan-8b8b11201/'>Linkedin</a></p>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align: center;'><a href='https://github.com/BintangRamadhan837'>GitHub</a></p>",
                unsafe_allow_html=True,
            )

            st.markdown("<hr>", unsafe_allow_html=True)

            st.markdown(
                "<h3 style='text-align: center;'>Rifky Aliffa</h3>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align: center;'><a href='https://www.linkedin.com/in/rifkyaliffa/'>Linkedin</a></p>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<p style='text-align: center;'><a href='https://github.com/Penzragon'>GitHub</a></p>",
                unsafe_allow_html=True,
            )

        st.markdown(
            "<p style='text-align: center;'>Made with <span style='color: red'>♥️</span> by <b>Kelompok 2</b></p>",
            unsafe_allow_html=True,
        )
