import streamlit as st
import pickle 
import pandas as pd
import numpy as np
import requests
from jikanpy import Jikan
import time
jikan = Jikan()

def fetch_poster(movie_id):
    path=jikan.anime(movie_id)
    return path['image_url']

def recommend(movie):
    index = anime[anime['name'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        # fetch the movie poster
        anime_id = anime['anime_id'][i[0]]
        recommended_movie_posters.append(fetch_poster(anime_id))
        recommended_movie_names.append(anime['name'][i[0]])

    return recommended_movie_names,recommended_movie_posters

similarity = pickle.load(open('similarity2.pkl','rb'))
anime = pickle.load(open('anime_n1.pkl','rb'))


st.title('Anime recommender System')
anime_list=list(anime['name'].values)
#print(anime_list)
selected_anime = st.selectbox('Select any of your favourite Anime',anime_list)
t = st.empty()


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters= recommend(selected_anime)
    col1, col2 = st.columns((2,2))
    with col1:
        st.write(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

        st.write(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

   
        st.write(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
   
        st.write(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    
        st.write(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col2:
        st.write(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

        st.write(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])

   
        st.write(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
   
        st.write(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    
        st.write(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])