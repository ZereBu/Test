import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

# Set wide layout
st.set_page_config(page_title="Pygwalker App", layout="wide")
st.title("🔎 Explora tus datos con Pygwalker")

# File uploader
uploaded_file = st.file_uploader("Sube un archivo CSV o Excel", type=["csv", "xlsx"])

if uploaded_file:
    # Load dataset
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### 👀 Vista previa del conjunto de datos")
    st.dataframe(df.head())

    # Add a manual reset button
    if st.button("🔄 Reiniciar explorador"):
        if "pygwalker_state" in st.session_state:
            del st.session_state["pygwalker_state"]

    st.write("### 📊 Explorador interactivo")
    renderer = StreamlitRenderer(df)
    # Only pass height — safe for all versions
    renderer.explorer(height=800)

else:
    st.info("⬆️ Sube un archivo CSV o Excel para comenzar a explorar")
