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
    (    'iron man 2008',
    'the incredible hulk',
    'iron man 2',
    'thor',
    'captain america the first avenger',
    'the avengers',
    'iron man 3',
    'thor the dark world',
    'captain america the winter soldier',
    'guardians of the galaxy',
    'avengers age of ultron',
    'daredevil',
    'ant man',
    'captain america civil war',
    'doctor strange',
    'guardians of the galaxy vol 2',
    'spider man homecoming',
    'thor ragnarok',
    'black panther',
    'avengers infinity war',
    'ant man the wasp',
    'captain marvel',
    'avengers endgame',
    'spider man far from home',
    'the falcon the winter soldier',
    'wandavision',
    'loki',
    'what if',
    'shang chi',
    'eternals',
    'hawkeye',
    'ms marvel',
    'moon knight',
    'she hulk', 
    'black widow',    
    'spider man no way home',    
    'doctor strange in the multiverse of madness',    
    'thor love and thunder',    
    'werewolf by night',
    'black panther wakanda forever'))

with st.spinner("loading model..."):
    new_model = tf.keras.models.load_model('model_lstm.h5')

response = api.search_recent_tweets(option)

tweets = response.data

#for tweet in tweets:
  #st.write(tweet.text)
  #st.write('----------------------------')

def get_sentiment(tweet):
  vocab_size = 50000
  max_length = 284
  oov_tok = "<OOV>"
  truc_type = 'post'
  tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
  tokenizer.fit_on_texts(tweet)
  pred_seq = tokenizer.texts_to_sequences(tweet)
  pred_padded = pad_sequences(pred_seq, maxlen=max_length, truncating=truc_type)
  scores = new_model.predict(pred_padded)
  return(scores)

count = 0

while (count<10):
    # get tweets (10 tweets)
    #tweets = api.search_recent_tweets('#crypto').data

    for tweet in tweets:
        original_tweet = tweet#.text
        #clean_tweet = preprocess_text(original_tweet)
        sentiment = get_sentiment(original_tweet)

        st.write('--------------------------------------------------------------------Tweet--------------------------------------------------------------------')
        st.write(original_tweet)
        st.write('---------------------------------------------------------------------------------------------------------------------------------------------')
        st.write('Sentiment:', sentiment)
        time.sleep(1)
        st.write('\n\n')
        count += 1