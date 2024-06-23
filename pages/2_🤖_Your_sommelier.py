import streamlit as st
import pandas as pd
from PIL import Image
from google.cloud import storage
from google.oauth2 import service_account
import io

st.set_page_config(initial_sidebar_state="collapsed")

@st.cache_data
def fetch_image_from_gcs(bucket_name, file_path):
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcs"])
    # Create a client using the specified credentials
    client = storage.Client(credentials=credentials)
    bucket = client.bucket(bucket_name)
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

if len(st.session_state.wine) > 4 :
    st.write("shuffling wines and returning 4")
elif len(st.session_state.wine) < 4 and len(st.session_state.wine) !=0 :
    st.write(f"returning only {len(st.session_state.wine)}wines")
elif len(st.session_state.final_pair) == 1 :
    st.write(f"returning most similar wine with highest {st.session_state.final_pair} score")
elif len(st.session_state.final_pair) == 2 :
    st.write(f"returning most similar wine with highest average {st.session_state.final_pair} score")
else :
    st.write(f"shuffling and returning most similar wines")
