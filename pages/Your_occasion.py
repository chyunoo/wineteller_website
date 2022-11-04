import streamlit as st
from page_config import standard_page_widgets
import requests
import pandas as pd


#- Handle legit mispells (diner x diner o)
#- Handle correct mispells (friend o friends x)


# Add this on top of any page to make mpa-config work!
standard_page_widgets()

st.sidebar.markdown("# The magic starts here 🪄")

if 'occasion' not in st.session_state:
    st.session_state.occasion = None





occasion = st.text_input('Describe your occasion in a few words.', help="ex : getting drunk with my friends" )

if occasion :
    st.session_state.occasion = occasion


if st.session_state.occasion is not None :

    st.write(f"Your current request is : {st.session_state.occasion}")






if st.button('Pair occasion'):

    #### run routine checks for occasion input
    #### no inputt -> "where are you headed to ?"
    #### occasion is not in list -> ask for another input + give examples
    #### if all tests succeed, run api

    with st.spinner('🤖 Sommelier at work ...'):

        params = dict(
            occasion = occasion)

        wineteller_url = "http://localhost:8000/predict"
        try :
            response = requests.get(wineteller_url, params=params)

            prediction = response.json()

            # @st.experimental_memo
            # def prediction_df(prediction) :
            #     res = pd.DataFrame.from_dict(prediction)
            #     return res

            # res = prediction_df(prediction)
            wines = {
                "Vin1" : [],
                "Vin2" : [],
                "Vin3" : [],
                "Vin4" : [],
                "Vin5" : [],
                "Vin6" : [],
                "Vin7" : [],
                "Vin8" : [],
                "Vin9" : [],
                "Vin10" : [],
            }
            i=1
            for item in prediction.values():
                for k, v in item.items():
                    wines["Vin" + str(i)] = item[k]
                i += 1


            res = pd.DataFrame.from_dict(prediction)

            # w1 = res.iloc[0]
            # w2 = res.iloc[1]
            # w3 = res.iloc[2]
            # w4 = res.iloc[3]
            # w5 = res.iloc[4]
            # w6 = res.iloc[5]
            # w7 = res.iloc[6]
            # w8 = res.iloc[7]
            # w9 = res.iloc[8]
            # w10 = res.iloc[9]
            #### if there is at least one recommendation -> st.write(check up your wine tab)
            #### print the prediction only if the prior test succeeds

            if len(res) > 0 :
                if 'res' not in st.session_state:
                    st.session_state.res = None
                st.session_state.res = res
                st.write("Your wines are ready !")

        except AttributeError :
            st.error("Hmm... Your sommelier doesn't seem to get that. Could you rephrase your occasion ?")
