import streamlit as st
st.logo("/Users/hyunoochang/code/chyunoo/wineteller/wineteller_website/utils/wineteller_logo_v1.png")
st.set_page_config(initial_sidebar_state="auto")
st.markdown("""
    # Hello, fellow wine lovers 👋

    ##### WineTeller🍷🥂 helps you find the right bottle of wine for your special occasion.

    We are the kind of people who believes that there are no **general guideline** for picking a decent bottle of wine and
    that anyone, **regardless of their knowledge** of wine, should be able to find a bottle that they will **trully appreciate**.

    We also believe that every bottle of wine is opened during **an unique moment**, and that wine is far
    more **enjoyable** when it is picked **accordingly to the occasion**.

    Thanks to Machine Learning techniques, **WineTeller**🍷🥂 is able to accurately pair **wine characteristics** (*is it bitter or smooth ?*) with
    the **tone** of an occasion (*are you home alone or hanging out with your friends ?*)
   """)


st.write("--")

st.markdown("""
    Wanna try it ?

    - **Type** the occasion you are about to encounter 👉 🥂 **Your occasion**, wait until the search is done 🤖

    - Then check your **wine recommendation** 👉 🍷 **Your wine**

    - Enjoy your wine 😋

    - If you have any enquiries about data or wine, feel free to say hi to 👉 🤖 **Your sommelier**

    """)
st.write("")

st.write("Cheers ! 😎")

st.write("--")

#### sign ponpon and louis #### (github links)
founder = '[Hyunoo](https://github.com/chyunoo)'
cofounder = '[Clément](https://github.com/ponpon32)'

st.caption(f" Kindly brought to you by {founder} and {cofounder}")
