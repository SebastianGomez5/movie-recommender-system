import pickle
import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import streamlit as st

# Cargar variables de entorno
load_dotenv()

#Conseguir poster
def fetch_poster(movie_id):
    api_key = os.getenv('TMDB_API_KEY')
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    else:
        return None  # o una imagen por defecto
    
def recommend(movie):    
    try:
        movie_index = movies[movies['original_title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        recommended_posters = []
        
        for i in movie_list:
            movie_id = movies.iloc[i[0]]['id']  # Columna correcta: 'id'
            movie_title = movies.iloc[i[0]]['original_title']
            
            recommended_movies.append(movie_title)
            poster_url = fetch_poster(movie_id)
            recommended_posters.append(poster_url if poster_url else "default_poster.jpg")
        
        return recommended_movies, recommended_posters
        
    except IndexError:
        return [], []
    except Exception as e:
        st.error(f"Error en recommend: {e}")
        return [], []

with st.sidebar:
    st.image("https://i.ibb.co/7CQVJNm/logo.png", width=200)
    st.title('Movie Recommender System')
    st.markdown("""
    This app recommends movies based on your favorite movie.
    
    **Instructions:**
    1. Select a movie from the dropdown.
    2. Click the 'Recommend' button to see similar movies.
    
    **Technologies Used:**
    - Python
    - Streamlit
    - Machine Learning
    - TMDB API
    
    **Developer:**
    - Sebastian Gomez
    """)
    
st.header('Movie Recommender System')
movies = pd.read_pickle('movies.pkl')
similarity = pd.read_pickle('similarity.pkl')
movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Recommend'):
    recommended_movies, recommended_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_posters[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_posters[4])