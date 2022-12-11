import streamlit as st
import tweepy
import re 
import time
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

bearer = "AAAAAAAAAAAAAAAAAAAAAGyskAEAAAAAfjx9FZsojIEN0WCN49M%2Bzzt%2Fvac%3DGAOdC50nuSLx78jtQpN8m9NoZibyVKsHsZYCG2zr5NYQw5t7VA"
consumer_key = "6dWgD1971DsRjSMRInEs8uNH7"
consumer_secret = "6e2XIBhR21Q82cTWgO1PP6u9tyrUhuZ0mMvs80dSQ6fX0eDgGj"
access_token = "980322159909257216-afpZwxHFcWQ4iTDMy25RSPflRK9wj7h"
access_token_secret = "7m05JbXOZOpD9aLQMwXDEBEYqqBYo2MAlO0fjA16s5j3W"

st.markdown("<h1 style='color: #22A7EC;'>Analisis Sentimen dari Tweets Terbaru</h1>", unsafe_allow_html=True)

api = tweepy.Client(bearer, consumer_key, consumer_secret, access_token, access_token_secret)
api.get_me()

option = st.selectbox(
    'Pilih film',
    ('Black Panther Wakanda Forever', 'Thor Love Thunder', 'Doctor Strange in the Multiverse of Madness'))

response = api.search_recent_tweets(option)

tweets = response.data


for tweet in tweets:
  st.write(tweet.text)
  st.write('----------------------------')