import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Hello Streamlit")

# Header
st.header("Netflix Movies and TV Shows")

# Write a greeting
st.write("Netflix stands as a leading force in the realm of media and video streaming. With a staggering array of over 8,000 movies and TV shows accessible on their platform, as of mid-2021, their global subscriber count exceeds 200 million. This tabulated dataset comprehensively catalogues all offerings on Netflix, including vital details such as cast, directors, ratings, release year, duration, and more.")

# Load CSV file with the appropriate encoding
try:
    df = pd.read_csv('netflix_titles.csv', encoding='ISO-8859-1')
except UnicodeDecodeError:
    st.error("There was an issue with the encoding of the CSV file.")

# Check if the dataframe is loaded successfully
if 'df' in locals():
    # Select only the first 12 columns
    df = df.iloc[:, :12]
    
    # Slider to control the number of rows displayed
    num_rows = st.slider('Number of rows to display', min_value=1, max_value=len(df), value=10)

    # Display the dataframe
    st.dataframe(df.head(num_rows))
