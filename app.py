# Import necessary libraries
import streamlit as st
import requests 

API_KEY = "7e3c7d3d"
BASE_URL = "http://www.omdbapi.com/"

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
