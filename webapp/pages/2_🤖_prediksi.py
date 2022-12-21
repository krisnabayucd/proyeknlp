import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

st.markdown("<h1 style='color: #22A7EC;'>Prediksi Sentimen Teks Ulasan</h1>", unsafe_allow_html=True)
st.write("#### masukkan teks ulasan yang ingin diprediksi sentimennya")

with st.spinner("loading model..."):
    new_model = tf.keras.models.load_model('model_lstm.h5')

#pred_review_text = st.text_input("masukkan teks")

form = st.form(key='my_form')
pred_review_text = form.text_input("masukkan teks")
form.form_submit_button('prediksi') 

if pred_review_text != '':
    pred = []
    pred.append(pred_review_text)
    with st.spinner("tokenizing text..."):
        vocab_size = 50000
        max_length = 284
        oov_tok = "<OOV>"
        truc_type = 'post'
        tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
        tokenizer.fit_on_texts(pred)
        pred_seq = tokenizer.texts_to_sequences(pred)
        pred_padded = pad_sequences(pred_seq, maxlen=max_length, truncating=truc_type)
    val = new_model.predict(pred_padded)
    new_val = str(val)
    st.subheader("hasil prediksi model: ")
    for i in range(0,len(pred)):
        st.write('teks input: '+ pred[i])
        st.write('skor sentimen: ' + str(val[i]))
        if val[i] > 0.5:
            st.write('positif')
        else:
            st.write('negatif')