import streamlit as st
import pandas as pd
import time
from utils.plot_wine import *
data = pd.read_csv('/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/scored_data.csv', index_col=0)

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
            st.page_link("pages/Your_wine.py", label="Your wines are ready !")
with col3:
    st.header("")

            #page_link = "[Go to another page](pages/Your_wine.py)"
            #st.success(f"Success! {page_link}")
            #start_time = time.time()
            #end_time = time.time()
            #execution_time = end_time - start_time
