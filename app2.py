import streamlit as st
import pyaudio
import numpy as np
import wave
import io
import torchaudio
import torch
import soundfile as sf
from audio_class import *
from reccomendation_system import *
from deepface import DeepFace
import cv2

# Load the image
emotion_labels = {
    'angry': 'Angry',
    'disgust': 'Disgust',
    'fear': 'Fear',
    'happy': 'Happy',
    'sad': 'Sad',
    'surprise': 'Surprise',
    'neutral': 'Neutral'
}

def facial_emotion(image):
    face_detections = DeepFace.analyze(image, actions=['emotion'],enforce_detection=False)
    emotions = face_detections[0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    emotion_label = emotion_labels[dominant_emotion]
    st.header((f"Your dominant emotion is {emotion_label}."))
# Function to capture image from webcam
def capture_image():
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (usually your webcam)

    if not cap.isOpened():
        st.error("Error: Webcam not found.")
        return

    # st.text("Capturing image...")
    ret, frame = cap.read()

    while ret:
        emotion=facial_emotion(frame)
        st.write(emotion)
        return emotion
    # Wait for the specified interval
        
    else:
        st.error("Error: Unable to capture an image.")

    cap.release()





# Set the layout to wide for better center alignment
st.set_page_config(layout="wide")

# Streamlit app title

    
st.markdown(""" <style> .font {
    font-size:80px ; font-family: 'Cooper Black'; color: #FF9633;text-align: left;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font" style="text-align: left;">NeuroSync Music</p>', unsafe_allow_html=True)
emo=capture_image()









# Create a function for each page
def home_page():
    
    
    
    


    
    
    
    st.header("We've songs for your mood: ")
    genre_list=['blue','rock']
    if emo=='neutral':
        genre_list=['blue','classical','country']
    elif emo=='anger':
        genre_list=['metal','blues','classical']
    elif emo=='fear':
        genre_list=['country','metal','jazz']
    elif emo=='happy':
        genre_list=['disco','pop','rock']
    elif emo=='disgust':
        genre_list=['blues','reggae','metal']
    elif emo=='surprise':
        genre_list=['hip-hop','disco','jazz']
    elif emo=='sad':
        genre_list=['country','classical','blues']
    st.table(recomend_artists(genre_list))


    # Define custom CSS for the musical theme
    search_box_css = """
    <style>
    .st-eb-search {
        background-color: #FF9633; 
        border: 8px solid #FF9633;
        border-radius: 25px;
        padding: 10px 20px; 
        color: #000000;
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
        ans=search_music(search_query)
        if ans is not None:
            st.write(ans)



   

    

# # Display the dataframe
    genres_list=['Pop','Rock','Classical']
    st.title("Your top Genres are: ")
    st.header(genres_list[0])
    st.header(genres_list[1])
    st.header(genres_list[2])
        
    

    middle_container = st.container()
    

    # Left and right columns in the middle container
    left_col, right_col = middle_container.columns(2)
    
    # Content on the left column
    with left_col:
        st.header("Get back to where you were,")
    # # Create a container in the middle of the page

    # # Sample data for the table
        data = [
                ["Boulevard of broken dreams", "Green Day", 2004],
                ["Castle of Glass", "Linkin Park", 2012],
                ["Yellow", "Coldplay", 2000],
                ["Desh Mere", "Arijit Singh", 2021],
                ["Putt Jatt Da", "Diljit Dosanjh", 2018],
                ]
        st.dataframe(data)
       
    def link_button(label, link):
        button = f'<a href="{link}" target="_blank"><button>{label}</button></a>'
        st.markdown(button, unsafe_allow_html=True)
    # # Content on the right column
    genres_list=['pop','rock','classical']
    artist_dict=recomend_artists(genres_list)
    artist_list=[]
    for i in artist_dict:
        artist_list.append(i)
    
    with right_col:
        st.header("Recomended artists: ")
        link_button(artist_list[0], artist_dict[artist_list[0]])
        link_button(artist_list[1], artist_dict[artist_list[1]])
        link_button(artist_list[2], artist_dict[artist_list[2]])
        link_button(artist_list[3], artist_dict[artist_list[3]])
        
    

    # Apply the custom CSS to the Streamlit container
    
    

 


def explore_audio():
    st.title("Explore music tracks")
    st.write("Explore the genres and emotions of tracks you're listening & singing")   
    st.write("Upload audio files yourself and explore genres")

    st.title("Classify your music tracks: ")
    
    uploaded_audio = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
    
    if uploaded_audio is not None:
        
        
        st.write("Uploaded audio file:")
        st.audio(uploaded_audio)
        st.title("predictions")
        res=find_class(uploaded_audio)
        # res2=find_emotions(uploaded_audio)
        st.header(res)
        # st.header(res2)
        
       
        


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
# selected_page = st.sidebar.radio("Select a Page", ["Home", "explore_audio", "Contact"])

# # Define custom CSS for the buttons
# button_css = """
# <style>
# .st-eb-button {
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     background-color: #FF9633;
#     color: #FFFFFF;
#     font-size: 24px;
#     font-weight: bold;
#     border: 2px solid #FF9633;
#     border-radius: 50%;
#     padding: 20px;
#     margin: 5px;
# }

# .st-eb-button:hover {
#     background-color: #FFB566;
# }
# </style>
# """

# # Apply the custom CSS
# st.markdown(button_css, unsafe_allow_html=True)

# # Create a sidebar section for selecting an icon
# st.sidebar.title("Select an Icon:")
# selected_icon = None
# if st.sidebar.button("Home"):
#     home_page()

# elif st.sidebar.button("explore_audio"):
#     explore_audio()

# elif st.sidebar.button("Contact"):
#     contact_page()
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
selected_tab = st.sidebar.radio("Select a page:", ("Home", "explore_audio", "Contact"))

# Create tabs and display the corresponding page content
if selected_tab == "Home":
    home_page()
elif selected_tab == "explore_audio":
    explore_audio()
elif selected_tab == "Contact":
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