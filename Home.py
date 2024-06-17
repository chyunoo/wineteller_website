import streamlit as st
st.logo("/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/wineteller_logo_v1.png")
st.set_page_config(initial_sidebar_state="auto")

st.markdown("""
    # Hello, wine lover 👋

    ### Wineteller helps you find the right bottle of wine for your special occasion.

    We are the kind of people who believes that anyone should be able to find the right wine.

    We also believe that every bottle of wine is opened during an unique moment that shapes its enjoyability.

    **Wineteller** uses data science to pair wine characteristics  with
    the tone of an occasion.
   """)


st.write("--")
your_occasion_page = "[Your occasion](pages/Your_occasion.py)"
your_wine_page = "[Your wine](pages/Your_wine.py)"
st.markdown(f"""
    ### Wanna try it ?

    - Describe your occasion 👉 🥂 Your occasion

    - Find your wine recommendation 👉 🍷 Your wine

    - Enjoy your moment 🍷🥂

    """)
st.write("")

st.write("--")

#### sign ponpon and louis #### (github links)
founder = '[Hyunoo](https://github.com/chyunoo)'
cofounder = '[Clément](https://github.com/ponpon32)'

st.caption(f" Born with {founder} and {cofounder}, raised by {founder}")
