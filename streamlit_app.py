import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(page_title="Pygwalker App", layout="wide")

st.title("🔎 Explora tus datos con Pygwalker")

uploaded_file = st.file_uploader("Sube un archivo CSV o Excel", type=["csv", "xlsx"])

if uploaded_file:
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

    st.write("### 👀 Vista previa del conjunto de datos")
    st.dataframe(df.head())

    # Add reset button
    if st.button("🔄 Resetear explorador"):
        if "pygwalker_state" in st.session_state:
            del st.session_state["pygwalker_state"]  # Clear pygwalker cache

    st.write("### 📊 Explorador interactivo")
    renderer = StreamlitRenderer(df)
    renderer.explorer(width=None, height=800, scrolling=True)

else:
    st.info("⬆️ Sube un archivo CSV o Excel para comenzar a explorar")
