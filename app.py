import streamlit as st
import pyaudio
import numpy as np
import wave
import io
import torchaudio
import torch
import soundfile as sf
from audio_class import *





# Set the layout to wide for better center alignment
st.set_page_config(layout="wide")

# Streamlit app title

    
    


st.markdown(""" <style> .font {
font-size:50px ; font-family: 'Cooper Black'; color: #FF9633;text-align: left;} 
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font" style="text-align: left;">NeuroSync Music</p>', unsafe_allow_html=True)

# Create a function for each page
def home_page():
    st.title("Welcome, Your today's mood:")
    st.header("We've songs for you: ")


    # Define custom CSS for the musical theme
    search_box_css = """
    <style>
    .st-eb-search {
        background-color: #FF9633; /* Background color */
        border: 8px solid #FF9633; /* Border color */
        border-radius: 25px; /* Rounded corners */
        padding: 10px 20px; /* Spacing */
        color: #000000; /* Text color */
        font-size: 20px; /* Text size */
        font-weight: bold; /* Text bold */
        font-family: 'Cursive', cursive; /* Font style */
    }

    .st-eb-search:hover {
        background-color: #FFB566; /* Hover color */
    }

    .st-eb-search:focus {
        outline: none; /* Remove focus border */
        border: 4px solid #FF9633; /* Restore border style on focus */
    }
    </style>
    """

    # Apply the custom CSS
    st.markdown(search_box_css, unsafe_allow_html=True)

    # Create a search box with the custom styling
    search_query = st.text_input("Search for music", value="", key="search")

    # Display the search results
    if st.button("Search"):
        st.write(f"You searched for: {search_query}")



    st.header("Get back to where you were,")
    # Create a container in the middle of the page

    # Sample data for the table
    data = [
        ["Boulevard of broken dreams", "Artist A", 2020],
        ["Song 2", "Artist B", 2019],
        ["Song 3", "Artist C", 2021],
        ["Song 4", "Artist A", 2018],
        ["Song 5", "Artist D", 2022],
    ]

    # Create a table with 5 rows
    st.dataframe(data)


    middle_container = st.container()

    # Left and right columns in the middle container
    left_col, right_col = middle_container.columns(2)

    # Content on the left column
    with left_col:
        st.header("Your top Genres are: ")
        st.write('genre1')
        st.write('genre2')
        st.write('genre3')

    # Content on the right column
    with right_col:
        st.header("Songs for you:")
        st.write("output of recommendations based on genres")

def explore_audio():
    st.title("Explore music tracks")
    st.write("Explore the genres and emotions of tracks you're listening & singing")   
    st.write("Upload audio files yourself and explore genres")

    st.title("Classify your music tracks: ")
    
    uploaded_audio = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
    
    st.write("Before")
    if uploaded_audio is not None:
        
        
        st.write("Uploaded audio file:")
        st.audio(uploaded_audio)
        st.write("after")
        st.title("predictions")
        res=find_class(uploaded_audio)
        st.write(res)
        
       
        


def contact_page():
    st.title("Your Profile")
    st.write("Bhavit Karnatak")
    st.write("email: unknown@example.com")
    st.write("Premium user")
    st.header("Contact Us:")
    st.write("write us at,")
    st.write("Email: contact@example.com")
    st.write("Phone: +123-456-7890")
    st.header("your stats:")

# Sidebar for page selection
selected_page = st.sidebar.radio("Select a Page", ["Home", "explore_audio", "Contact"])

# Define custom CSS for the buttons
button_css = """
<style>
.st-eb-button {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #FF9633;
    color: #FFFFFF;
    font-size: 24px;
    font-weight: bold;
    border: 2px solid #FF9633;
    border-radius: 50%;
    padding: 20px;
    margin: 5px;
}

.st-eb-button:hover {
    background-color: #FFB566;
}
</style>
"""

# Apply the custom CSS
st.markdown(button_css, unsafe_allow_html=True)

# Create a sidebar section for selecting an icon
st.sidebar.title("Select an Icon:")
selected_icon = None
if st.sidebar.button("Home"):
    home_page()

elif st.sidebar.button("explore_audio"):
    explore_audio()

elif st.sidebar.button("Contact"):
    contact_page()

# Define custom CSS for the login box
login_box_css = """
<style>
.st-eb-login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 300px;
    background-color: #ECECEC;
    border: 2px solid #FF9633;
    border-radius: 15px;
    padding: 20px;
    margin: auto;
}

.st-eb-login-title {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

.st-eb-login-input-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 5px 0;
    width: 100%; /* Make the input boxes equally sized */
}

.st-eb-login-input {
    padding: 10px;
    border: 2px solid #FF9633;
    border-radius: 5px;
    width: 100%; /* Make the input boxes equally sized */
}

.st-eb-login-button {
    background-color: #FF9633;
    color: #FFFFFF;
    font-size: 18px;
    font-weight: bold;
    border: none;
    border-radius: 5px;
    padding: 10px;
    cursor: pointer;
}

.st-eb-login-button:hover {
    background-color: #FFB566;
}

.st-eb-login-button:focus {
    outline: none;
}
</style>
"""

# Apply the custom CSS
# st.markdown(login_box_css, unsafe_allow_html=True)

# # Create an attractive login box
# st.title("Login")
# with st.container():
#     st.markdown("<h2 class='st-eb-login-title'>Welcome to My Music App</h2>", unsafe_allow_html=True)
#     username = st.text_input("Username", key="username", class="st-eb-login-input")
#     password = st.text_input("Password", key="password", type="password", class="st-eb-login-input")
#     login_button = st.button("Login", class="st-eb-login-button")

# if login_button:
#     # You can add login logic here
#     if username == "example" and password == "password":
#         st.success("Login successful")
#     else:
#         st.error("Invalid username or password")