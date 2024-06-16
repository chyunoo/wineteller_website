import streamlit as st

import pandas as pd

# Add this on top of any page to make mpa-config work!

if 'occasion' in st.session_state :
    st.write(st.session_state.occasion)

"I am a future feature 🥷"
