import streamlit as st
import pickle
import pandas as pd
import requests

# This commented blocks are for movie posters. Which is not available in India
# def fetch_poster(movie_id):
#     response = requests.get('http://api.themoviedb.org/3/movie/{'
#                             '}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data = response.json()
#     return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    # recommended_movies_poster = []
    for i in movies_list:
        movie_id = i[0]

        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from API
        # recommended_movies_poster.append(fetch_poster(i[0]))
    return recommended_movies       #, recommended_movies_poster

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Which Movie would you like to search?',movies['title'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)