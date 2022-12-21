import streamlit as st

st.set_page_config(
    page_title = "Analaisis Sentimen",
    page_icon = "🏠",
)

st.markdown("<h1 style='color: #22A7EC;'>Analisis Sentimen Film Marvel (MCU)</h1>", unsafe_allow_html=True)
st.sidebar.success("pilih halaman")

from PIL import Image
image = Image.open('marvel.jpg')

st.image(image, caption='~')

st.markdown('Aplikasi ini ditujukan untuk analisis sentimen film MCU berdasarkan tweets dan ulasan dari IMDB. Model yang digunakan adalah LSTM yang telah dilatih dengan 50000 data ulasan film yang bersumber dari IMDB. Klik sidebar di samping untuk menampilkan fitur-fitur dari aplikasi')