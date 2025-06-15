# Import necessary libraries
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API key securely
load_dotenv()
API_KEY = os.getenv("OMDB_API_KEY")
BASE_URL = "http://www.omdbapi.com/"

def fetch_movies(search_term):
    response = requests.get(f"{BASE_URL}?apikey={API_KEY}&s={search_term}")
    data = response.json()
    return data.get("Search", [])  # Return movie list or empty list

# Streamlit UI
st.title("🎬 Movie Search App")
search_query = st.text_input("Enter a movie title", "")

if search_query:
    movies = fetch_movies(search_query)
    
    if movies:
        for movie in movies:
            poster_url = movie["Poster"]
            
            # ✅ Use a placeholder if poster is not available
            if poster_url == "N/A":
                poster_url = "https://via.placeholder.com/300x450.png?text=No+Poster"

            st.image(poster_url, width=500)
            st.subheader(movie["Title"])
            st.write(f"Year: {movie['Year']}")
    else:
        st.error("No movies found. Try another search!")

st.markdown("<hr><small>Developed by @Pawan Yadav ©</small>", unsafe_allow_html=True)
