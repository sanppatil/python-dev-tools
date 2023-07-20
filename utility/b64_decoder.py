import streamlit as st
from st_pages import add_page_title
from base64 import b64decode

add_page_title(layout="wide")

st.subheader("Base64 Encoded Text")
input_string = st.text_area('Encoded Text', 'V29yayBpdCwgbWFrZSBpdCwgZG8gaXQsIG1ha2VzIHVzOiBoYXJkZXIsIGJldHRlciwgZmFzdGVyLCBzdHJvbmdlciE=', 
    max_chars=10000, height=200, label_visibility="collapsed")

st.subheader("Plain Text")
input_string_bytes = b64decode(input_string)
st.write(input_string_bytes.decode("UTF-8"))

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)