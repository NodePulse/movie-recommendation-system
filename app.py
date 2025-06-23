import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("MY_API_KEY")

# Load data
movies = pickle.load(open("movies.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

st.title("🎬 Movie Recommendation System")
st.markdown("""
Welcome to the **Movie Recommendation System**! 🎥🍿  
This app helps you discover movies similar to your favorite ones using content-based filtering.  
Simply choose a movie from the dropdown, and it will suggest 5 similar movies along with their posters.

**Features:**
- Instant recommendations from a curated movie dataset
- Movie posters fetched live from TMDB (The Movie Database)
- Clean, interactive UI built with Streamlit

🔍 Powered by machine learning and cosine similarity.
""")

# Function to fetch poster from TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]  # Top 5 excluding the selected movie

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]]['id']
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# Streamlit select box
selected_movie_name = st.selectbox(
    "Choose a movie to get recommendations 👇",
    movies['title'].values
)

# When button is clicked
if st.button("🎯 Recommend"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx])
            st.caption(names[idx])
