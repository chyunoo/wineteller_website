import streamlit as st
import pandas as pd
from utils.plot_wine import *
st.logo("/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/wineteller_logo_v1.png")
st.set_page_config(initial_sidebar_state="collapsed")
dtype_dict = {
    'country': 'category',
    'province': 'category',
    'variety': 'category',
    'romantic_sc' : 'float32',
    'fancy_sc' : 'float32',
    'moody_sc' : 'float32',
    'casual_sc' : 'float32',
    'avg_sc' : 'float32',
    'romantic_sc_norm' : 'uint8',
    'fancy_sc_norm' : 'uint8',
    'casual_sc_norm' : 'uint8',
    'moody_sc_norm' : 'uint8'
}
@st.cache_data
def load_scored_data() :
    return pd.read_csv('/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/scored_data.csv',
                   index_col=0,
                   dtype=dtype_dict
                   )

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
            filtered_wine = filter_wine(load_scored_data(), processed_input)
            st.session_state.wine = filtered_wine

            if 'wine' in st.session_state and 'processed_input' in st.session_state :
                #wine = st.session_state.wine
                #processed_input = st.session_state.processed_input
                your_wine = pair_wine(load_scored_data(), filtered_wine, processed_input)
                print(your_wine)
                st.session_state.your_wine = your_wine
                st.page_link("pages/3_🍷_Your_wine.py", label="Your wines are ready !")
with col3:
    st.header("")

            #page_link = "[Go to another page](pages/Your_wine.py)"
            #st.success(f"Success! {page_link}")
            #start_time = time.time()
            #end_time = time.time()
            #execution_time = end_time - start_time
