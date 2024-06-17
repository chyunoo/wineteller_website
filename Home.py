import streamlit as st
from PIL import Image
from google.cloud import storage
from google.oauth2 import service_account
import io

st.set_page_config(initial_sidebar_state="auto")

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

st.markdown("""
    # Hello, wine lover 👋

    ### Wineteller helps you find the right bottle of wine for your special occasion.

    We are the kind of people who believes that anyone should be able to find the right wine.

    We also believe that every bottle of wine is opened during an unique moment that shapes its enjoyability.

    **Wineteller** uses data science to pair wine characteristics  with
    the tone of an occasion.
   """)


st.write("--")
your_occasion_page = "[Your occasion](pages/Your_occasion.py)"
your_wine_page = "[Your wine](pages/Your_wine.py)"
st.markdown(f"""
    ### Wanna try it ?

    - Describe your occasion 👉 🥂 Your occasion

    - Find your wine recommendation 👉 🍷 Your wine

    - Enjoy your moment 🍷🥂

    """)
st.write("")

st.write("--")

#### sign ponpon and louis #### (github links)
founder = '[Hyunoo](https://github.com/chyunoo)'
cofounder = '[Clément](https://github.com/ponpon32)'

st.caption(f" Born with {founder} and {cofounder}, raised by {founder}")
