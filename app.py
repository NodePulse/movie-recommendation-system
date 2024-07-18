import streamlit as st
import pickle
# import requests

movies = pickle.load(open("movies.pkl", 'rb'))
with open('similarity.pkl') as fin:
    pickle.load(fin)

st.title("Movie Recommendation System")

# def fetch_poster(movie_id):
#     response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=d832395be4f69b0fb93e41c73843f195&language=en-US".format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie, movies):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    # recommended_movies_poster = []
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        # recommended_movies_poster.append(fetch_poster(i[0]))
    # return recommended_movies, recommended_movies_poster
    return recommended_movies

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

if st.button("Recommend", type="primary"):
    # recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name, movies)
    recommended_movie_names = recommend(selected_movie_name, movies)
    for i in recommended_movie_names:
        st.write(i)
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
