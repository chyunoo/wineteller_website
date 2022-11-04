import streamlit as st
from page_config import standard_page_widgets

import pandas as pd

# Add this on top of any page to make mpa-config work!
standard_page_widgets()

if 'occasion' in st.session_state :
    st.write(st.session_state.occasion)
