import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

api_key = os.getenv("MY_API_KEY")

movies = pickle.load(open("movies.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

st.title("Movie Recommendation System")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)
    response = requests.get(url)
    data = response.json()
    # poster_path = data['poster_path']
    # full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    # return full_path

# print(fetch_poster(64))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(i[0]))
        print(i[0])
    # return recommended_movies, recommended_movies_poster
    return recommended_movies

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

# recommend("Avatar", movies)
print(fetch_poster(1321))

# if st.button("Recommend", type="primary"):
    # recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name, movies)
    # recommended_movie_names = recommend(selected_movie_name, movies)
    # for i in recommended_movie_names:
        # st.write(i)
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(recommended_movie_names[0])
    #     st.image(recommended_movie_posters[0])
        
    # with col2:
    #     st.text(recommended_movie_names[1])
    #     st.image(recommended_movie_posters[1])

    # with col3:
    #     st.text(recommended_movie_names[2])
    #     st.image(recommended_movie_posters[2])
    # with col4:
    #     st.text(recommended_movie_names[3])
    #     st.image(recommended_movie_posters[3])
    # with col5:
    #     st.text(recommended_movie_names[4])
    #     st.image(recommended_movie_posters[4])