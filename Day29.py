import streamlit as st
import pandas as pd

# Import for API calls
import requests

# Import for navbar
from streamlit_option_menu import option_menu

# Import for dynamic tagging
from streamlit_tags import st_tags, st_tags_sidebar

# Imports for aggrid
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid import GridUpdateMode, DataReturnMode

# Import for loading interactive keyboard shortcuts into the app
from dashboard_utils.gui import keyboard_to_url
from dashboard_utils.gui import load_keyboard_class

if "widen" not in st.session_state:
    layout = "centered"
else:
    layout = "wide" if st.session_state.widen else "centered"

st.set_page_config(layout=layout, page_title="Zero-Shot Text Classifier", page_icon="🤗")

st.image("Logo.png", width=350)

st.title("Zero-Shot Text Classifier")


#Ca va nous servir à utiliser les différents types de modes
with st.sidebar:
    selected = option_menu(
        "",
        ["Demo", "Unlocked Mode"],
        icons=["bi-joystick", "bi-key-fill"],
        menu_icon="",
        default_index=0,
    )


if selected == "Demo":
    None
elif selected=="Unlocked Mode":
    if st.secrets['API_token'] == 'None':
        with st.form(key="my_form"):
            API_KEY2 = st.text_input(
                "Enter your 🤗 HuggingFace API key",
                help="Once you created you HuggiginFace account, you can get your free API token in your settings page: https://huggingface.co/settings/tokens",
            )

            API_URL = (
                "https://api-inference.huggingface.co/models/valhalla/distilbart-mnli-12-3"
            )

            headers = {"Authorization": f"Bearer {API_KEY2}"}
            
    
            api_token = API_KEY2

            label_widget = st_tags(
                    label="",
                    text="Add labels - 3 max",
                    value=["Transactional", "Informational"],
                    suggestions=[
                        "Navigational",
                        "Transactional",
                        "Informational",
                        "Positive",
                        "Negative",
                        "Neutral",
                    ],
                    maxtags=3,
                )
            new_line = "\n"
            nums = [
                    "I want to buy something in this store",
                    "How to ask a question about a product",
                    "Request a refund through the Google Play store",
                    "I have a broken screen, what should I do?",
                    "Can I have the link to the product?",
                    ]

            sample = f"{new_line.join(map(str, nums))}"

            linesDeduped2 = []
            
            MAX_LINES = 5
            text = st.text_area(
                "Enter keyphrases to classify",
                sample,
                height=200,
                key="2",
                help="At least two keyphrases for the classifier to work, one per line, "
                + str(MAX_LINES)
                + " keyphrases max as part of the demo",
                )
            lines = text.split("\n")  # A list of lines
            linesList = []
            for x in lines:
                linesList.append(x)
            linesList = list(dict.fromkeys(linesList))  # Remove dupes
            linesList = list(filter(None, linesList))  # Remove empty

            if len(linesList) > MAX_LINES:

                st.info(
                    f"❄️  Only the first "
                    + str(MAX_LINES)
                    + " keyprases will be reviewed. Unlock that limit by switching to 'Unlocked Mode'"
                )

            linesList = linesList[:MAX_LINES]
            st.form_submit_button()



def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    # Unhash to check status codes from the API response
    # st.write(response.status_code)
    return response.json()


listToAppend = []
for row in linesList:
    output2 = query(
                {
                    "inputs": row,
                    "parameters": {"candidate_labels": label_widget},
                    "options": {"wait_for_model": True},
                }
            )
    listToAppend.append(output2)
df=pd.DataFrame.from_dict(listToAppend)

gb = GridOptionsBuilder.from_dataframe(df)
# enables pivoting on all columns, however i'd need to change ag grid to allow export of pivoted/grouped data, however it select/filters groups
gb.configure_default_column(
    enablePivot=True, enableValue=True, enableRowGroup=True
)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_side_bar()  # side_bar is clearly a typo :) should by sidebar
gridOptions = gb.build()

response = AgGrid(
    df,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    height=400,
    fit_columns_on_grid_load=False,
    configure_side_bar=True,
)