import streamlit as st
from page_config import standard_page_widgets
img_path = "/Users/hyunoochang/Desktop/blank.jpg"

# Add this on top of any page to make mpa-config work!
standard_page_widgets()


# - Add 'description' column in final output
# - Add sidebar description for sommelier and wine
# - Add white, red, rosé feature






if 'res' in st.session_state :
    res = st.session_state.res
    res.columns = ["Country", "Province", "Region", "Variety"]
    res.reset_index(inplace=True, drop=True)
    res.index = res.index + 1
    #st.dataframe(res)
    # for k, v in prediction.items() :
    #     print(type(v))
    #     st.write(k)
    #     wine = ""
    #     for item in v.values() :
    #         wine += item + " "
    #     st.write(wine)
    # for wine in res.iterrows() :
    #     st.dataframe(wine)
    w1 = res.take([0])
    w2 = res.take([1])
    w3 = res.take([2])
    w4 = res.take([3])
    w5 = res.take([4])
    w6 = res.take([5])
    w7 = res.take([6])
    w8 = res.take([7])
    w9 = res.take([8])
    w10 = res.take([9])
    # st.write(w1)
    # st.write(w1.iloc[0,1])

    st.write("----")
    # with st.spinner('🤖 Sommelier at work ...'):
    c1, c2= st.columns([0.75,8])
    with st.container():
        with c1 :
            st.image(img_path,
             width=None)
        with c2 :
            st.markdown(f"""
                    🌐 **{w1.iloc[0,0]}**

                    📍 {w1.iloc[0,2]}, {w1.iloc[0,1]}

                    🍇 { w1.iloc[0,3]}
                    """)
    st.write("--")
    c3, c4 = st.columns([0.75,8])
    with st.container():
        with c3 :
            st.image(img_path,
             width=None)
        with c4 :
            st.markdown(f"""
                    🌐 **{w2.iloc[0,0]}**

                    📍 {w2.iloc[0,2]}, {w2.iloc[0,1]}

                    🍇 {w2.iloc[0,3]}
                    """)
    st.write("--")
    c5, c6 = st.columns([0.75,8])
    with st.container():
        with c5 :
            st.image(img_path,
             width=None)
        with c6 :
            st.markdown(f"""
                    🌐 **{w3.iloc[0,0]}**

                    📍 {w3.iloc[0,2]}, {w3.iloc[0,1]}

                    🍇 {w3.iloc[0,3]}
                    """)
    st.write("--")
    c7, c8 = st.columns([0.75,8])
    with st.container():
        with c7 :
            st.image(img_path,
             width=None)
        with c8 :
            st.markdown(f"""
                    🌐 **{w4.iloc[0,0]}**

                    📍 {w4.iloc[0,2]}, {w4.iloc[0,1]}

                    🍇 {w4.iloc[0,3]}
                    """)
    st.write("--")
    c9, c10 = st.columns([0.75,8])
    with st.container():
        with c9 :
            st.image(img_path,
             width=None)
        with c10 :
            st.markdown(f"""
                    🌐 **{w5.iloc[0,0]}**

                    📍 {w5.iloc[0,2]}, {w5.iloc[0,1]}

                    🍇 {w5.iloc[0,3]}
                    """)
    st.write("----")

else :
    None
