import streamlit as st
from st_pages import add_page_title
import utilities

add_page_title(layout="wide")

st.subheader("Base64 Encoded Text")
input_string = st.text_area('Encoded Text', 'V29yayBpdCwgbWFrZSBpdCwgZG8gaXQsIG1ha2VzIHVzOiBoYXJkZXIsIGJldHRlciwgZmFzdGVyLCBzdHJvbmdlciE=', 
    max_chars=10000, height=200, label_visibility="collapsed")

st.subheader("Plain Text")
st.write(utilities.base64_decode(input_string))