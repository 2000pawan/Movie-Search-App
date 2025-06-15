# 📦 Import required libraries
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# 🔐 Load API key from environment variable
load_dotenv()
API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "http://www.omdbapi.com/"
PLACEHOLDER_POSTER = "https://via.placeholder.com/300x450.png?text=No+Poster"

def fetch_movies(search_term):
    response = requests.get(f"{BASE_URL}?apikey={API_KEY}&s={search_term}")
    data = response.json()
    return data.get("Search", [])  # Return movie list or empty list

st.title("🎬 Movie Search App")
search_query = st.text_input("Enter a movie title", "")

if search_query:
    movies = fetch_movies(search_query)
    
    if movies:
        for movie in movies:
            poster_url = movie["Poster"]
            
            # ✅ Skip movies with "N/A" posters
            if poster_url == "N/A":
                continue  
            
            st.image(poster_url, width=500)
            st.subheader(movie["Title"])
            st.write(f"Year: {movie['Year']}")
    else:
        st.error("No movies found. Try another search!")
st.write("Developed by @ Pawan Yadav")
