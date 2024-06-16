import streamlit as st

import pandas as pd

# Add this on top of any page to make mpa-config work!

if 'occasion_input' not in st.session_state:
    st.session_state.occasion_input = None
    st.write("I am a future feature 🥷")
else :
    st.write(f""" How romantic : {st.session_state.occasion_input[0]},
             How moody : {st.session_state.occasion_input[1]},
             How casual : {st.session_state.occasion_input[2]},
             How fancy : {st.session_state.occasion_input[3]}""")
