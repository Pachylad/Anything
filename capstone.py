# Import Libraries

import streamlit as st
import os
import numpy as np
import pandas as pd
import requests
import pickle
from sklearn.metrics.pairwise import cosine_similarity

api_key =os.getenv("apikey")

thirty_thou_dict = pickle.load(open("thirty_thou.pkl","rb"))
thirty_thou = pd.DataFrame(thirty_thou_dict)
thirtythou_new_dict = pickle.load(open("thirtythou_new.pkl","rb"))
thirtythou_new = pd.DataFrame(thirtythou_new_dict)

similarity = cosine_similarity(thirtythou_new)

def recommend(song, artist):
    index = thirty_thou[(thirty_thou['track_name'] == song) & (thirty_thou['track_artist'] == artist)].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(thirty_thou.iloc[i[0]]['track_name'] + ' by ' + thirty_thou.iloc[i[0]]['track_artist'])


# def fetch_artist?(movie_id):
#    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
#    data = response.json()
#   print(data)
#    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


# ''' Frontend '''

v = st.write(""" <h2> <b style="color:red"> MoviesWay</b> </h2>""",unsafe_allow_html=True)
# st.header(v)
# st.header(" :red[MoviesWay]")
st.write("###")

st.write(""" <p> Hii, welcome to <b style="color:red">Moviesway</b> this free movie recommendation engine suggests films based on your interest </p>""",unsafe_allow_html=True)
st.write("##")
my_expander = st.expander("Tap to Select a Song  🌐️")
selected_song_name = my_expander.selectbox("",thirty_thou["track_name"].values)
selected_artist_name = my_expander.selectbox("",thirty_thou["track_artist"].values)

if my_expander.button("Recommend"):
    st.text("Here are few Recommendations..")
    st.write("#")
    recommend(selected_song_name,selected_artist_name)
#    col1,col2,col3,col4,col5=st.columns(5)
#    cols=[col1,col2,col3,col4,col5]
#    for i in range(0,5):
#            with cols[i]:
#                st.write(f' <b style="color:#E50914"> {names[i]} </b>',unsafe_allow_html=True)
                


#future release
# with st.sidebar:
#     st.write("Moviesway🍿")

st.write("##")
tab1 ,tab2 = st.tabs(["About","Working"])

with tab1:
    st.caption('This a Content Based Movie Recommendation System')
    st.caption('In upcoming versions new movies would be added 😎')   #:blue[:sunglasses:]
with tab2:
    st.caption("It Contains Movie's from The Movie Data Base (TMDB)")
    st.caption("For more infos and ⭐ at https://github.com/vikramr22/moviesway-v2 ")

