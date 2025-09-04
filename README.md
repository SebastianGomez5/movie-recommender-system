# Movie Recommender System
#### Application Preview
![App Screenshot](https://i.ibb.co/27GcT1Lt/Captura-de-pantalla-2025-09-03-225510.jpg){:width="800px"}
*Main interface showing movie selection and recommendations*

A simple movie recommendation system that suggests similar movies based on your preferences. Powered by Machine Learning (Based on cosine similarity) y Streamlit.

## Technologies Used
- **Python** 3.11+
- **Streamlit** - Web interface
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine Learning
- **CountVectorizer** - Word processing
- **Cosine Similarity** - Recommendation algorithm
- **TMDB API** - Movie and image data

## Installation
```git
# Clone repository
git clone https://github.com/SebastianGomez5/movie-recommender-system

cd movie-recommender-system

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Advanced settings
#### Environment variables
Create a file `.env`
```
# Get your API key from: https://www.themoviedb.org/settings/api
TMDB_API_KEY=your_api_key_here
```

##  Dataset

This project uses the **TMDB 5000 Movie Dataset** from Kaggle:
- **Source**: [TMDB Movie Metadata on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Contains**: 5000 movies with metadata, ratings, and credits
- **License**: CC BY-NC-SA 4.0 (Check Kaggle for current license terms)

The dataset includes:
- `tmdb_5000_movies.csv` - Movie metadata and details
- `tmdb_5000_credits.csv` - Cast and crew information

## Developer
Sebastian Gomez
- **Github**: [@SebastianGomez5](https://github.com/SebastianGomez5)
- **Linkedin**: [Sebastian Gomez](https://www.linkedin.com/in/sebastian-g%C3%B3mez-885814337/)