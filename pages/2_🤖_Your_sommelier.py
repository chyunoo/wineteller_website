import streamlit as st

import pandas as pd
st.logo("/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/wineteller_logo_v1.png")
st.set_page_config(initial_sidebar_state="collapsed")

if 'occasion_input' not in st.session_state:
    st.write("I am a future feature 🥷")

else :
    st.write(f""" How romantic : {st.session_state.occasion_input[0]},
             How moody : {st.session_state.occasion_input[1]},
             How casual : {st.session_state.occasion_input[2]},
             How fancy : {st.session_state.occasion_input[3]}""")
