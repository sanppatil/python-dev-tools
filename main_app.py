import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

show_pages(
    [
        Page("main_app.py", "Dev Tools", "🏠"),
        Section(name="Files", icon=":gear:"),
        Page("utilities/csv_viewer.py", "CSV Viewer", ":mag:"),
        Section(name="Utilities", icon=":gear:"),
        Page("utilities/b64_encoder.py", "Base64 Encoder", ":mag:"),
        Page("utilities/b64_decoder.py", "Base64 Decoder", ":mag:"),
        Section(name="Security", icon=":gear:"),
        Page("utilities/jwt_viewer.py", "JWT Viewer", ":key:"),
    ]
)

add_page_title()  # Optional method to add title and icon to current page

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)