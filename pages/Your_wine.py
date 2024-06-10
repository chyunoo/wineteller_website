import streamlit as st
from page_config import standard_page_widgets
from utils.plot_wine import *
# Add this on top of any page to make mpa-config work!
standard_page_widgets()

data = pd.read_csv('/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/scored_data.csv', index_col=0)

# - Add 'description' column in final output
# - Add sidebar description for sommelier and wine
# - Add white, red, rosé feature

if 'wine' in st.session_state and 'processed_input' in st.session_state :
    wine = st.session_state.wine
    processed_input = st.session_state.processed_input
    recommendation = pair_wine(data, wine, processed_input)

st.pyplot(fig=recommendation, clear_figure=False)
