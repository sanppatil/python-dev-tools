import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

show_pages(
    [
        Page("main_app.py", "Dev Tools", "🏠"),
        Section(name="Files", icon=":gear:"),
        Page("utility/csv_viewer.py", "CSV Viewer", ":mag:"),
        Section(name="Utilities", icon=":gear:"),
        Page("utility/b64_encoder.py", "Base64 Encoder", ":mag:"),
        Page("utility/b64_decoder.py", "Base64 Decoder", ":mag:"),
        Section(name="Security", icon=":gear:"),
        Page("security/jwt_viewer.py", "JWT Viewer", ":key:"),
        Page("security/aes_encrypter.py", "AES Encryption", ":key:"),
        Page("security/aes_decrypter.py", "AES Decryption", ":key:"),
    ]
)

add_page_title()  # Optional method to add title and icon to current page

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)