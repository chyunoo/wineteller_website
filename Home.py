import streamlit as st
from page_config import standard_page_widgets

# Add this on top of any page to make mpa-config work!
standard_page_widgets()

# st.set_page_config(
#     page_title="Wineteller",
#     page_icon="🍷🥂",
#     layout="centered",
#     initial_sidebar_state="expanded")

# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
#add_bg_from_local('/Users/hyunoochang/Downloads/wineteller2.jpg')

#title = st.text_input('What occasion ?', )

# st.sidebar.markdown(f"""
#     # Header resizer
#     """)

#st.sidebar.markdown("# <font color='grey'>  Hello 👋 </font>",unsafe_allow_html=True)
st.sidebar.markdown("# Pairing wine with moment 🍾")
st.markdown("""
    # Hello, fellow wine lover 👋

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



#### sign ponpon and louis #### (github links)
