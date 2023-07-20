import streamlit as st
from st_pages import add_page_title
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

add_page_title(layout="wide")

st.subheader("Encrypted Text")
encrypted_text = st.text_area('Encrypted Text', '3b09+y6d1SGrBRhIzpQnO0Xd+A3RkQ39cbUxodjY6bEmxB3A/OjJvHySJ0dvM4I0BMIMMIIi3AiGF1SmeaEFq5yQ7CHynEuwNAl8DLFN51QAtsZB7NOa/MIRKla0NEWLm/+8nnzbiLQTEHbKmc6fmKN9P/Y7tLk4aAVAdWe8fP1TKmbLyotTYWyCjm7org3a', 
    max_chars=5000, height=100, label_visibility="collapsed", on_change=None)
encrypted_text_bytes = b64decode(encrypted_text)

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
st.subheader("Plain Text")
if encryption_mode == "ECB":
    cipher = AES.new(secret_key_bytes, AES.MODE_ECB)
else:
    cipher = AES.new(secret_key_bytes, AES.MODE_CBC, initialization_vector_bytes)

plain_text = unpad(cipher.decrypt(encrypted_text_bytes), AES.block_size)

st.write(plain_text.decode("UTF-8"))