import streamlit as st
import pickle
import pandas as pd

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_df = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend_movie(movie_title):
    movie_index = movies_df[movies_df['title'] == movie_title].index[0]
    distances = list(enumerate(similarity[movie_index]))
    ls = sorted(distances,reverse=True,key=lambda x:x[1])[1:11]
    result = []
    for ind in ls:
        result.append(movies_df.iloc[ind[0]].title)
    return  result

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select your favorite movie",
    movies_df['title'].values,
)

if st.button("Recommend"):
    recommendation = recommend_movie(selected_movie_name)
    ind = 1
    for title in recommendation:
        with st.container(horizontal=True,gap="small"):
            st.write(ind)
            st.write(title)
            ind = ind + 1