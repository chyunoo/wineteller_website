import streamlit as st
from utils.plot_wine import *


data = pd.read_csv('/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/scored_data.csv', index_col=0)

# Inject custom CSS to reduce tab container size
st.markdown(
    """
    <style>
    .stTabs {
        max-width: 50%; /* Adjust the maximum width of the tab container */
        font-size: 12px; /* Adjust the font size of the tab labels */
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'wine' in st.session_state and 'processed_input' in st.session_state :
    wine = st.session_state.wine
    processed_input = st.session_state.processed_input
    your_wine = pair_wine(data, wine, processed_input)
    print(your_wine)


tab1, tab2, tab3, tab4 = st.tabs(["Wine 1", "Wine 2", "Wine 3", "Wine 4"])

with tab1:
   #st.header("A cat")
   your_wine_plot = plot_wine_recommendations([your_wine[0][0]], [your_wine[1][0]], [your_wine[2][0]])
   st.pyplot(fig=your_wine_plot, clear_figure=False)

   with st.expander("See explanation"):
        st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
        ''')

with tab2:
   #st.header("A cat")
   your_wine_plot = plot_wine_recommendations([your_wine[0][1]], [your_wine[1][1]], [your_wine[2][1]])
   st.pyplot(fig=your_wine_plot, clear_figure=False,use_container_width=True)

   with st.expander("See explanation"):
        st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
        ''')

with tab3:
   #st.header("A cat")
   your_wine_plot = plot_wine_recommendations([your_wine[0][2]], [your_wine[1][2]], [your_wine[2][2]])
   st.pyplot(fig=your_wine_plot, clear_figure=False)

   with st.expander("See explanation"):
        st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
        ''')

with tab4:
   #st.header("A cat")
   your_wine_plot = plot_wine_recommendations([your_wine[0][3]], [your_wine[1][3]], [your_wine[2][3]])
   st.pyplot(fig=your_wine_plot, clear_figure=False)

   with st.expander("See explanation"):
        st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
        ''')
