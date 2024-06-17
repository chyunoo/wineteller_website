import streamlit as st
from utils.plot_wine import *
from PIL import Image
from google.cloud import storage
from google.oauth2 import service_account
import io

st.set_page_config(initial_sidebar_state="collapsed")

credentials = st.secrets["connections.gcs"]
@st.cache_data
def fetch_image_from_gcs(bucket_name, file_path):
    credentials = service_account.Credentials.from_service_account_file(credentials)
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

# Inject custom CSS to reduce tab container size
st.markdown(
    """
    <style>
    .stTabs {
        max-width: 50%; /* Adjust the maximum width of the tab container */
        font-size: 14px; /* Adjust the font size of the tab labels */
    }
    </style>
    """,
    unsafe_allow_html=True
)
if 'your_wine' in st.session_state :
    your_wine = st.session_state.your_wine

tab1, tab2, tab3, tab4 = st.tabs(["Wine 1", "Wine 2", "Wine 3", "Wine 4"])

with tab1:
   your_wine_plot = plot_wine_recommendations([your_wine[0][0]], [your_wine[1][0]], [your_wine[2][0]])
   your_wine_description = your_wine[2][0]

   st.subheader(f"{your_wine_description[-2]}, {your_wine_description[-1]}")
   st.pyplot(fig=your_wine_plot, clear_figure=False)
   st.write(f"🍇 : {your_wine_description[2]}")
   st.write(f"🔑words : {your_wine_description[1][1:-1]}")

   with st.expander("Description"):
        st.write(your_wine_description[0])

with tab2:
   your_wine_plot = plot_wine_recommendations([your_wine[0][1]], [your_wine[1][1]], [your_wine[2][1]])
   your_wine_description = your_wine[2][1]

   st.subheader(f"{your_wine_description[-2]}, {your_wine_description[-1]}")
   st.pyplot(fig=your_wine_plot, clear_figure=False,use_container_width=True)
   st.write(f"🍇 : {your_wine_description[2]}")
   st.write(f"🔑words : {your_wine_description[1][1:-1]}")

   with st.expander("Description"):
        st.write(your_wine_description[0])

with tab3:
   your_wine_plot = plot_wine_recommendations([your_wine[0][2]], [your_wine[1][2]], [your_wine[2][2]])
   your_wine_description = your_wine[2][2]

   st.subheader(f"{your_wine_description[-2]}, {your_wine_description[-1]}")
   st.pyplot(fig=your_wine_plot, clear_figure=False)
   st.write(f"🍇 : {your_wine_description[2]}")
   st.write(f"🔑words : {your_wine_description[1][1:-1]}")

   with st.expander("Description"):
        st.write(your_wine_description[0])

with tab4:
   your_wine_plot = plot_wine_recommendations([your_wine[0][3]], [your_wine[1][3]], [your_wine[2][3]])
   your_wine_description = your_wine[2][3]

   st.subheader(f"{your_wine_description[-2]}, {your_wine_description[-1]}")
   st.pyplot(fig=your_wine_plot, clear_figure=False)
   st.write(f"🍇 : {your_wine_description[2]}")
   st.write(f"🔑words : {your_wine_description[1][1:-1]}")

   with st.expander("Description"):
        st.write(your_wine_description[0])
