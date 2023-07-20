import streamlit as st
from st_pages import add_page_title
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

add_page_title(layout="wide")

st.subheader("Plain Text")
plain_text = st.text_area('Plain Text', 'Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve.', 
    max_chars=5000, height=100, label_visibility="collapsed", on_change=None)
plain_text_bytes = bytes(plain_text, encoding='utf-8')

col1, col2 = st.columns(2)
with col1:
    encryption_mode = st.selectbox('Encryption Mode',["CBC", "ECB"])
with col2:
    key_size_in_bits = st.selectbox('Key Size in Bits',[128, 256])
    key_size_in_bytes = key_size_in_bits//8

col1, col2 = st.columns(2)
with col1:
    if encryption_mode == "ECB":
        initialization_vector = st.text_input('Initialization Vector', 'N/A', max_chars=key_size_in_bytes, disabled = True)
    else:
        initialization_vector = st.text_input('Initialization Vector', 'init_vect_sample', max_chars=key_size_in_bytes)
    initialization_vector_bytes = bytes(initialization_vector, encoding='utf-8')
with col2:
    secret_key = st.text_input('Secret Key', 'secret_ky_sample', max_chars=key_size_in_bytes)
    secret_key_bytes = bytes(secret_key, encoding='utf-8')
st.divider()
st.subheader("Encrypted Text")
if encryption_mode == "ECB":
    cipher = AES.new(secret_key_bytes, AES.MODE_ECB)
else:
    cipher = AES.new(secret_key_bytes, AES.MODE_CBC, initialization_vector_bytes)

encrypted_text_bytes = cipher.encrypt(pad(plain_text_bytes, AES.block_size))
encrypted_text_b64 = b64encode(encrypted_text_bytes)
st.write(encrypted_text_b64.decode("UTF-8"))

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)