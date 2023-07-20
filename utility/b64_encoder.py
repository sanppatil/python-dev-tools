import streamlit as st
from st_pages import add_page_title
from base64 import b64encode

add_page_title(layout="wide")


st.subheader("Plain Text")
input_string = st.text_area('Plain Text', "And if at first your don't succeed, then dust yourself off and try again!", 
    max_chars=10000, height=200, label_visibility="collapsed")

st.subheader("Base64 Encoded Text")
output_b64_bytes = b64encode(input_string.encode("UTF-8"))
st.write(output_b64_bytes.decode("UTF-8"))