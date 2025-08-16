from httpx import URL
import streamlit as st
import pandas as pd 

import requests

URL = "https://viacep.com.br/ws/{cep}/json/"

st.title("Busque Cep")

cep = st.text_input("Busque seu cep")

if cep != "":
    resp = requests.get(URL.format(cep=cep))
    data = pd.DataFrame([resp.json()])
    st.dataframe(data)