import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe_file = pd.read_csv(uploaded_file)
    st.dataframe(dataframe_file, use_container_width=True, hide_index=True, height=500)