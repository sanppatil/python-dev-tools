import streamlit as st
from st_pages import add_page_title
from base64 import b64decode
import jwt
import json

add_page_title(layout="wide")

encoded_token = st.text_area('Encoded Token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiJodHRwczovL3NlcnZpY2VidXMuYXp1cmUubmV0IiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzgwZjE3ZTctOTgxOS00Nzg4LWEyMDItMmFkOTkzMTQzZTg4LyIsImlhdCI6MTY4OTY5ODY1OCwibmJmIjoxNjg5Njk4NjU4LCJleHAiOjE2ODk3MDI1NTgsImFpbyI6IkUyWmdZQWorUGZQa2pwblp4MW1yUGg4dHEyTGFEZ0E9IiwiYXBwaWQiOiI1MTdiODQ3Mi1lNTMzLTQ2ZDctYTM1Ni1lN2IwMzQwN2NhYjAiLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83ODBmMTdlNy05ODE5LTQ3ODgtYTIwMi0yYWQ5OTMxNDNlODgvIiwib2lkIjoiZWNlMjY1MWEtZDAzZi00YzhjLTlhNTgtMTk1ZjcxMjhmZTQ3IiwicmgiOiIwLkFWa0E1eGNQZUJtWWlFZWlBaXJaa3hRLWlQa09vWUJvZ1QxSnFfa3lsOFR2Ymp5ZEFBQS4iLCJzdWIiOiJlY2UyNjUxYS1kMDNmLTRjOGMtOWE1OC0xOTVmNzEyOGZlNDciLCJ0aWQiOiI3ODBmMTdlNy05ODE5LTQ3ODgtYTIwMi0yYWQ5OTMxNDNlODgiLCJ1dGkiOiJrTHdQTXlOQWMwNmtTUXhZQUg1OUFBIiwidmVyIjoiMS4wIn0.RMfFg-DjcE4Q302r4qV0B3AvO--5sWK4EfpAogM8y_YRn3SgoPIQVKuH3vW0deHslh3XBNzPRXF9DHz32V20V5Df4scbXK3GMlYjODpbA87CknBEBTw2O6m9atDn0wazuzCjk3NovLxt0DJa5mCASIUpmXDUkW2vXNLr2_s-_D-bi8EzMbSmngW6k5Bl14nVam-74szFYbgeqMo2IvG2-UUu2e-6b1HBImLbubiOFQhO8zZnJbRRtYsiD346zq-LkiZdaS80mOzN97VUxsyE-8nlM2rATpjjI1GDVtBPZzfONijs0nlhKBP80Q53TW4bWivshNT6RztfZdA-fEWmkA', 
    max_chars=5000, height=200)

token_parts = encoded_token.split(".")

st.subheader("Header")
jwt_header = json.loads(b64decode(token_parts[0]))
st.json(jwt_header)

st.subheader("Payload")
st.json(jwt.decode(jwt=encoded_token, options={"verify_signature": False}))

st.subheader("Signature")
algorithm = jwt_header["alg"]
st.write(token_parts[2])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)