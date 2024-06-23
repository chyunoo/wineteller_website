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
def return_score_descriptors(highest_occasion) :
    score_descriptors = {
    "romantic" : ["flowers", "notes", "lilac", "violet_rose"],
    "moody" : ["wood", "notes", "oak", "toasted_coconut"],
    "casual" : ["medium_body", "style", "racy", "fruity"],
    "fancy" : ["refined", "style", "flashy", "elegant"]
    }
    if len(highest_occasion) == 1 :
        index = highest_occasion[0].index("sc")
        highest_occasion_str = highest_occasion[0][:index-1]
        highest_occasion_descriptors = score_descriptors[highest_occasion_str]
    else :
        indices = [i.index("sc") for i in highest_occasion]
        highest_occasion_str = [highest_occasion[i][:indices[i]-1] for i in range(len(indices))]
        highest_occasion_descriptors = [score_descriptors[highest_occasion_str[i]] for i in range(len(highest_occasion_str))]
    return highest_occasion_str, highest_occasion_descriptors


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
            text = f"""You requested a wine with : {occasion_input_text}.
            \nWe found {len(st.session_state.wine)} matches ({round(len(st.session_state.wine)/st.session_state.len_dataset,2)}%) !
            \nShuffling wines and returning 4.
                """
            st.write_stream(stream_data(text))
        elif len(st.session_state.wine) < 4 and len(st.session_state.wine) !=0 :
            text = f"""You requested a wine with : {occasion_input_text}
            \nWe found {len(st.session_state.wine)} matches.
            \nReturning only {len(st.session_state.wine)} wines.
            """
            st.write_stream(stream_data(text))
        elif len(st.session_state.final_pair) == 1 :
            highest_occasion_text = return_score_descriptors(st.session_state.final_pair)
            if highest_occasion_text[0] in ("romantic","moody") :
                text = f"""You requested a {highest_occasion_text[0]} wine with : {occasion_input_text}.
                \n{highest_occasion_text[0]} wines are characterized by {highest_occasion_text[1][0]} {highest_occasion_text[1][1]}, like {highest_occasion_text[1][2]} or  {highest_occasion_text[1][3]}.
                \nWe found {len(st.session_state.wine)} matches.
                \nSearching similar wines with same average score : {st.session_state.input_average}/4 ...
                \nReturning most similar wines with highest {st.session_state.final_pair[0][:-8]} score : {st.session_state.avg_final_selection}/1.
                """
            else :
               text =f"""You requested a {highest_occasion_text[0]} wine with : {occasion_input_text}.
                \n{highest_occasion_text[0]} wines are characterized by a {highest_occasion_text[1][0]} {highest_occasion_text[1][1]}, they are {highest_occasion_text[1][2]} and {highest_occasion_text[1][3]}.
                \nWe found {len(st.session_state.wine)} matches.
                \nSearching similar wines with same average score : {st.session_state.input_average}/4 ...
                \nReturning most similar wines with highest {st.session_state.final_pair[0][:-8]} score : {st.session_state.avg_final_selection}/1.
               """
            st.write_stream(stream_data(text))
        elif len(st.session_state.final_pair) == 2 :
            highest_occasion_text = return_score_descriptors(st.session_state.final_pair)
            text = f"""You requested a {highest_occasion_text[0][0]} and {highest_occasion_text[0][1]} wine with : {occasion_input_text}.
            \n{highest_occasion_text[0][0]} wines are characterized by {highest_occasion_text[1][0][0]} {highest_occasion_text[1][0][1]} ({highest_occasion_text[1][0][2]}, {highest_occasion_text[1][0][3]}) and
            \n{highest_occasion_text[0][1]} wines are characterized by {highest_occasion_text[1][1][0]} {highest_occasion_text[1][1][1]} ({highest_occasion_text[1][1][2]}, {highest_occasion_text[1][1][3]}).
            \nWe found {len(st.session_state.wine)} matches.
            \nSearching similar wines with same average score :  {st.session_state.input_average}/4 ...
            \nCalculating average {[i[:-8] for i in st.session_state.final_pair]} score ...
            \nReturning most similar wine with highest average {[i[:-8] for i in st.session_state.final_pair]} score : {st.session_state.avg_final_selection}/1.
            """
            st.write_stream(stream_data(text))
        elif len(st.session_state.final_pair) == 0 :
            text = f"""You requested a wine with : {occasion_input_text}.
            \nWe found {len(st.session_state.wine)} matches.
            \nSearching similar wines with same average score : {st.session_state.input_average}/4 ...
            \nShuffling and returning 4 most similar wines.
            """
            st.write_stream(stream_data(text))
    else :
        text = f"""Hello, please request an occasion
        """
        st.write_stream(stream_data(text))
