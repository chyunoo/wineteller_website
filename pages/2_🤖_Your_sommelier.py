import streamlit as st
import pandas as pd
from PIL import Image
from google.cloud import storage
import io

st.set_page_config(initial_sidebar_state="collapsed")

@st.cache_data
def fetch_image_from_gcs(bucket_name, file_path):
    bucket = storage.Client().bucket(bucket_name)
    blob = bucket.blob(file_path)
    image_data = blob.download_as_bytes()
    return image_data
# Fetch image data from GCS
logo_data = fetch_image_from_gcs("scored_data_1706", "wineteller_logo_v1.png")
# Convert binary data to PIL Image
logo = Image.open(io.BytesIO(logo_data))
st.logo(logo)

if 'occasion_input' not in st.session_state:
    st.write("I am a future feature 🥷")
else :
    st.write(f""" How romantic : {st.session_state.occasion_input[0]},
             How moody : {st.session_state.occasion_input[1]},
             How casual : {st.session_state.occasion_input[2]},
             How fancy : {st.session_state.occasion_input[3]}""")
