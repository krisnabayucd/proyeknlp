import streamlit as st

st.set_page_config(
    page_title = "Analaisis Sentimen Ulasan Film",
    page_icon = "🏠",
)

st.title('Analisis Sentimen Film Marvel')
st.sidebar.success("pilih halaman")

from PIL import Image
image = Image.open('marvel.jpg')

st.image(image, caption='~')

st.markdown('Aplikasi ini ditujukan untuk analisis sentimen film MCU. Model yang digunakan adalah LSTM yang telah dilatih dengan 50000 data ulasan film. Klik sidebar di samping untuk menampilkan fitur-fitur dari aplikasi')