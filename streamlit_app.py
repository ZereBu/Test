import streamlit as st
import pandas as pd
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(page_title="Pygwalker App", layout="wide")

st.title("🔎 Explore your Data with Pygwalker")

# Upload data
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Load dataset
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### 👀 Dataset Preview")
    st.dataframe(df.head())

    st.write("### 📊 Interactive Explorer")
    # Render Pygwalker explorer
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()
else:
    st.info("⬆️ Upload a CSV or Excel file to start exploring")
