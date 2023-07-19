import streamlit as st
from st_pages import add_page_title
import utilities

add_page_title(layout="wide")

st.subheader("Plain Text")
input_string = st.text_area('Plain Text', "And if at first your don't succeed, then dust yourself off and try again!", 
    max_chars=10000, height=200, label_visibility="collapsed")

st.subheader("Base64 Encoded Text")
st.write(utilities.base64_encode(input_string))