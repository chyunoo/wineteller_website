import streamlit as st
from page_config import standard_page_widgets
import requests
import pandas as pd
import time
from utils.plot_wine import *
data = pd.read_csv('/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/scored_data.csv', index_col=0)

# Add this on top of any page to make mpa-config work!
standard_page_widgets()

st.sidebar.markdown("# The magic starts here 🪄")

if 'occasion_input' not in st.session_state:
    st.session_state.occasion_input = None

romantic_input = st.slider("How romantic ?", min_value=1, max_value=4, step=1)
st.write(romantic_input)
moody_input = st.slider("How moody ?", min_value=1, max_value=4,  step=1)
casual_input = st.slider("How casual ?", min_value=1, max_value=4, step=1)
fancy_input = st.slider("How fancy ?", min_value=1, max_value=4, step=1)
occasion_input = [romantic_input, moody_input, casual_input, fancy_input]

if occasion_input :
    st.session_state.occasion_input = occasion_input

#if st.session_state.occasion_input is not None :
    #st.write(f"Your current request is : {st.session_state.occasion_input}")

if st.button('Pair occasion'):

    #### run routine checks for occasion input
    #### no inputt -> "where are you headed to ?"
    #### occasion is not in list -> ask for another input + give examples
    #### if all tests succeed, run api

    with st.spinner('🤖 Sommelier at work ...'):

        start_time = time.time()
        processed_input = process_input(occasion_input)
        st.session_state.processed_input = processed_input
        filtered_wine = filter_wine(data, processed_input)
        if 'res' not in st.session_state:
            st.session_state.res = None
        st.session_state.wine = filtered_wine
        st.write("Your wines are ready !")
        end_time = time.time()
        execution_time = end_time - start_time
        st.write(f"execution_time :{execution_time:.2f} seconds")
