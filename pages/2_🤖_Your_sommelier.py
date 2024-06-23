import streamlit as st
import pandas as pd
from PIL import Image
from google.cloud import storage
from google.oauth2 import service_account
import io
import time

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

#if 'occasion_input' not in st.session_state:
#    st.write("🤖 : error_can't_find_occasion")

def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)
if 'occasion_input' in st.session_state:
    occasion_input_text = f""" How romantic : {st.session_state.occasion_input[0]},
             How moody : {st.session_state.occasion_input[1]},
             How casual : {st.session_state.occasion_input[2]},
             How fancy : {st.session_state.occasion_input[3]}"""

with st.chat_message("user", avatar="🤖"):
    if 'wine' in st.session_state:
        if len(st.session_state.wine) >= 4 :
            text = f"""You requested a wine with : {occasion_input_text}
            \nwe found {len(st.session_state.wine)} matches ({round(len(st.session_state.wine)/st.session_state.len_dataset,2)}%)
            \nshuffling wines and returning 4
                """
            st.write_stream(stream_data(text))
        elif len(st.session_state.wine) < 4 and len(st.session_state.wine) !=0 :
            text = f"""You requested a wine with : {occasion_input_text}
            \nwe found {len(st.session_state.wine)} matches
            \nreturning only {len(st.session_state.wine)}wines
            """
            st.write_stream(stream_data(text))
        elif len(st.session_state.final_pair) == 1 :
            text = f"""You requested a wine with : {occasion_input_text}
            \nwe found {len(st.session_state.wine)} matches
            \nsearching similar wines with same average score : {st.session_state.input_average}
            \nreturning most similar wines with highest {st.session_state.final_pair} score : {st.session_state.avg_final_selection}
            """
            st.write_stream(stream_data(text))
        elif len(st.session_state.final_pair) == 2 :
            text = f"""You requested a wine with : {occasion_input_text}
            \nwe found {len(st.session_state.wine)} matches
            \nsearching similar wines with same average score :  {st.session_state.input_average}
            \ncalculating average {st.session_state.final_pair} score
            \nreturning most similar wine with highest average {st.session_state.final_pair} score : {st.session_state.avg_final_selection}
            """
            st.write_stream(stream_data(text))
        elif len(st.session_state.final_pair) == 0 :
            text = f"""You requested a wine with : {occasion_input_text}
            \nwe found {len(st.session_state.wine)} matches
            \nsearching similar wines with same average score : {st.session_state.input_average}
            \nshuffling and returning 4 most similar wines
            """
            st.write_stream(stream_data(text))
    else :
        text = f"""Hello, please request an occasion
        """
        st.write_stream(stream_data(text))
