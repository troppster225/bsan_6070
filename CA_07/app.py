import streamlit as st
import pandas as pd
import pickle

#loading the serialized model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

#loading the saved scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

df = pd.read_csv('https://github.com/ArinB/MSBA-CA-Data/raw/main/CA05/movies_recommendation_data.csv')

genre_columns = ['Biography', 'Drama', 'Thriller', 'Comedy', 'Crime', 'Mystery', 'History']

st.title("Movie Recommender")

selected_genres = st.multiselect("Select Genres:", genre_columns)

imdb_rating = st.slider("IMDB Rating:", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Get Recommendations"):
    input_vector = [1 if genre in selected_genres else 0 for genre in genre_columns]
    standardized_rating = scaler.transform([[imdb_rating]])[0][0]
    input_vector = [standardized_rating] + input_vector

    distances, indices = model.kneighbors([input_vector], n_neighbors=5)

    st.subheader("Top 5 Recommended Movies:")
    for idx in indices[0]:
        movie = df.iloc[idx]
        st.write(f"**{movie['Movie Name']}** - IMDB Rating: {movie['IMDB Rating']}")