import streamlit as st
import pandas as pd
from utils.plot_wine import *
from st_files_connection import FilesConnection
from PIL import Image
from google.cloud import storage
from google.oauth2 import service_account
import io

st.set_page_config(initial_sidebar_state="collapsed")
conn = st.connection('gcs', type=FilesConnection)
data = conn.read("scored_data_1706/scored_data.csv", input_format="csv", ttl=600)
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

st.sidebar.markdown("# The magic starts here 🪄")

col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("")
   romantic_input = st.slider("How romantic ?", min_value=1, max_value=4, step=1)
with col2:
   st.header("")
   moody_input = st.slider("How moody ?", min_value=1, max_value=4,  step=1)
with col3:
   st.header("")
   casual_input = st.slider("How casual ?", min_value=1, max_value=4, step=1)
with col4:
   st.header("")
   fancy_input = st.slider("How fancy ?", min_value=1, max_value=4, step=1)

col1, col2, col3 = st.columns(3)
with col1:
   st.header("")
with col2:
    st.header("")

    on = st.toggle("Pair occasion")
    if on:
        occasion_input = [romantic_input, moody_input, casual_input, fancy_input]
        st.session_state.occasion_input = occasion_input
        with st.spinner('🤖 Sommelier at work ...'):

            processed_input = process_input(occasion_input)
            st.session_state.processed_input = processed_input
            filtered_wine = filter_wine(data, processed_input)
            st.session_state.wine = filtered_wine

            if 'wine' in st.session_state and 'processed_input' in st.session_state :
                your_wine = pair_wine(data, filtered_wine, processed_input)
                st.session_state.your_wine = your_wine
                st.page_link("pages/3_🍷_Your_wine.py", label="Your wines are ready !")
with col3:
    st.header("")
