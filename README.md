# Movie Search App

## 📌 Overview
The **Movie Search App** is a simple **Streamlit** web application that allows users to search for movies using the **OMDb API**. It displays the **movie title, release year, and poster** while filtering out movies without valid poster images.

## 🚀 Features
- 🔍 **Search for Movies**: Enter a search term to find relevant movies.
- 🖼️ **Displays Movie Posters**: Only shows movies with valid poster images.
- 🌐 **Uses OMDb API**: Fetches real-time movie data.
- ✅ **Filters Out Missing Posters**: Prevents errors by skipping movies with missing posters.
- ⚡ **Fast and Simple UI**: Built using **Streamlit** for a smooth experience.

## 📦 Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/2000pawan/Movie-Search-App.git
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Get an OMDb API Key**
- Visit [OMDb API](https://www.omdbapi.com/) and sign up for an API key.
- Replace `YOUR_API_KEY` in the code with your actual key.

## 🛠️ Usage
### **Run the App**
```bash
streamlit run app.py
```

### **Search for Movies**
1. Open the **Streamlit app** in your browser.
2. Enter a **movie name** in the search bar.
3. The app will display **movies with valid posters**.

## 📌 Example Output
| Movie Title         | Year  | Poster  |
|---------------------|------|---------|
| Sholay             | 1975 | 🖼️ |
| The Sholay Girl    | 2019 | 🖼️ |
| Ramgarh Ke Sholay  | 1991 | 🖼️ |

(*Movies without posters are skipped to prevent errors.*)

## ⚠️ Troubleshooting
**Error: `MediaFileStorageError: Error opening 'N/A'`**
- This happens when the app tries to display a movie without a valid poster.
- The app now automatically **skips movies with missing posters**.

**API Key Issues**
- If the API request fails, check if:
  - Your API key is correct.
  - You haven't exceeded the request limit.

## 📝 License
This project is **open-source** under the **MIT License**.

## 🤝 Contributing
- Fork the repository.
- Create a new branch (`feature-branch`).
- Commit changes and create a pull request.

## 📞 Contact
- **Author**: Pawan Yadav
- **Email**: yaduvanshi2000pawan@gmail.com

