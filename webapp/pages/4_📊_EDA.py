import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import numpy as np

#title
st.title('Eksplorasi dan Visualisasi Data')
#markdown
st.markdown('Halaman ini menampilkan sejumlah visualisasi dan bagan dari sentimen')
#sidebar
st.sidebar.title('Visualisasi dari Keseluruhan Sentimen')

data=pd.read_csv('reviews.csv')
#checkbox to show data 
if st.checkbox("Show Data"):
    st.write(data.head(50))

#selectbox + visualisation

# Multiple widgets of the same type may not share the same key.
select=st.sidebar.selectbox('pilih jenis grafik',['Histogram','Pie Chart'],key=0)
sentiment=data['sentiment'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Reviews':sentiment.values})
st.markdown("###  Sentiment count")
if select == "Histogram":
        fig = px.bar(sentiment, x='Sentiment', y='Reviews', color = 'Reviews', height= 500)
        st.plotly_chart(fig)
else:
        fig = px.pie(sentiment, values='Reviews', names='Sentiment')
        st.plotly_chart(fig)


#multiselect
st.sidebar.subheader("Visulasi Sentimen per Film")
choice = st.sidebar.multiselect("pilih film yang ingin dibandingkan", (    'iron man',
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
    'ant man and the wasp',
    'captain marvel',
    'avengers endgame',
    'spider man far from home',
    'the falcon and the winter soldier',
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
    'black panther wakanda forever'), key = '1')  
if len(choice)>0:
    air_data=data[data.film.isin(choice)]
    # facet_col = 'sentiment'
    fig1 = px.histogram(air_data, x='film', y='sentiment', histfunc='count', color='sentiment',labels={'sentiment':'reviews'}, height=600, width=800)
    st.plotly_chart(fig1)

#subheader
st.sidebar.subheader('Sampel Ulasan')
#radio buttons
reviews=st.sidebar.radio('pilih jenis sentimen',('positive','negative','neutral'))
st.markdown('###  reviews samples:')
st.write(data.query('sentiment==@reviews')[['review']].sample(1).iat[0,0])
st.markdown('####  ========================================================')
st.write(data.query('sentiment==@reviews')[['review']].sample(1).iat[0,0])
st.markdown('####  ========================================================')
st.write(data.query('sentiment==@reviews')[['review']].sample(1).iat[0,0])
st.markdown('####  ========================================================')

