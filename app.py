# 📦 Import required libraries
import streamlit as st
import requests

# 🔐 Load API key securely from Streamlit secrets
API_KEY = st.secrets["OMDB_API_KEY"]
BASE_URL = "http://www.omdbapi.com/"
PLACEHOLDER_POSTER = "https://via.placeholder.com/300x450.png?text=No+Poster"

# 🎯 Function to fetch movies using partial match
def fetch_movies(search_term):
    response = requests.get(f"{BASE_URL}?apikey={API_KEY}&s={search_term}")
    data = response.json()

    if data.get("Response") == "True":
        # Optional: filter for better match
        return [movie for movie in data["Search"] if search_term.lower() in movie["Title"].lower()]
    else:
        return []

# 🖼️ Streamlit UI Setup
st.set_page_config(page_title="🎬 Movie Search App", layout="centered")
st.title("🎬 Movie Search App")
st.markdown("Search for your favorite movies and view their posters and release year.")

# 🔍 Movie search box
search_query = st.text_input("Enter a movie title")

if search_query:
    movies = fetch_movies(search_query.strip())

    if movies:
        for movie in movies:
            poster_url = movie["Poster"] if movie["Poster"] != "N/A" else PLACEHOLDER_POSTER

            # 🎞️ Display movie info
            st.image(poster_url, width=300)
            st.subheader(movie["Title"])
            st.write(f"🗓️ Year: {movie['Year']}")
            st.markdown("---")
    else:
        st.warning("❌ No movies found. Please try a different search term.")

# 📄 Footer
st.markdown("<hr><small>Developed by <b>@Pawan Yadav</b> | © 2025</small>", unsafe_allow_html=True)
