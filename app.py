from utils import utils
import streamlit as st
from PIL import Image
from lyrics import lyris_generator


# Setup your config
utils.page_config()
utils.style_app()


# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("LyricalMuse")
st.markdown("This app helps you to generate original song lyrics tailored to their chosen mood, theme, genre, and any additional specifications.")

# Setting up the sidebar for input
st.sidebar.title("LyricalMuse - Lyzr.ai")
API_KEY = st.sidebar.text_input("Enter your OpenAI API key", type='password')

if API_KEY != "":

    col1, col2, col3 = st.columns(3)

    with col1:
        Mood = st.selectbox(label='Select Mood', options=['None', 'happy', 'sad', 'angry', 'romantic', 'nostalgic'])

    with col2:
        Theme = st.selectbox(label='Select Theme', options=['None', 'love', 'loss', 'self-discovery', 'social commentary'])

    with col3:
        Genre = st.selectbox(label='Select Genre', options=['None', 'pop', 'rock', 'rap', 'hip-hop', 'country'])


    if (Mood or Theme or Genre) != 'None':
        if st.button('Submit'):
            generated_output = lyris_generator(api_key=API_KEY, mood=Mood, theme=Theme, genre=Genre)
            lyrics = generated_output[0]['task_output']
            if lyrics:
                st.markdown('---')
                st.write(lyrics)


st.sidebar.markdown('---')
utils.template_end()
utils.social_media()