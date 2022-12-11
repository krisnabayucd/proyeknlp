import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

st.title('Dashboard Analisis Sentimen Film')

st.markdown('Aplikasi ini dapat digunakan untuk menilai sentimen suatu film berdasarkan data twitter')

st.sidebar.title('Exploratory Data Analysis')
st.sidebar.markdown('sidebar')

data=pd.read_csv('tweet.csv')

if st.checkbox("show data"):
    st.write(data.head(20))

st.sidebar.subheader('Analisis')
tweets=st.sidebar.radio('Tipe Sentimen',('positive','negative','neutral'))
st.write(data.query('sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('sentiment==@tweets')[['text']].sample(1).iat[0,0])

select=st.sidebar.selectbox('Visualisation Of Tweets',['Histogram','Pie Chart'],key=1)
sentiment=data['sentiment'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})
st.markdown("###  Sentiment count")
if select == "Histogram":
        fig = px.bar(sentiment, x='Sentiment', y='Tweets', color = 'Tweets', height= 500)
        st.plotly_chart(fig)
else:
        fig = px.pie(sentiment, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)

#slider
st.sidebar.markdown('Time & Location of tweets')
hr = st.sidebar.slider("Hour of the day", 0, 23)
data['Date'] = pd.to_datetime(data['tweet_created'])
hr_data = data[data['Date'].dt.hour == hr]
if not st.sidebar.checkbox("Hide", True, key='1'):
    st.markdown("### Location of the tweets based on the hour of the day")
    st.markdown("%i tweets during  %i:00 and %i:00" % (len(hr_data), hr, (hr+1)%24))
    st.map(hr_data)

#multiselect
st.sidebar.subheader("Film tweets by sentiment")
choice = st.sidebar.multiselect("Film", (''), key = '0')  
if len(choice)>0:
    air_data=data[data.film.isin(choice)]

    fig1 = px.histogram(film_data, x='film', y='sentiment', histfunc='count', color='sentiment',labels={'sentiment':'tweets'}, height=600, width=800)
    st.plotly_chart(fig1)
