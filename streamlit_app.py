import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd

st.set_page_config(layout="wide")
st.title("Explora tus datos con PyGWalker (tamaño personalizado)")

uploaded = st.file_uploader("Sube un archivo CSV o Excel", type=["csv","xlsx"])
if uploaded:
    df = pd.read_csv(uploaded) if uploaded.name.endswith(".csv") else pd.read_excel(uploaded)
    st.dataframe(df.head())

    renderer = StreamlitRenderer(df)
    renderer.explorer(width=1200, height=800, scrolling=True)
else:
    st.info("⬆️ Sube un archivo para comenzar")
