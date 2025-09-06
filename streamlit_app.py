import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(page_title="Pygwalker Multi-CSV App", layout="wide")
st.title("🔎 Explora tus datos con PyGWalker")

# 1️⃣ Correct RAW GitHub URLs
csv_files = {
    "Amongus": "https://raw.githubusercontent.com/ZereBu/Test/main/amogus%20(2)%20(1)%20(1).xlsx",
    "Kpop": "https://raw.githubusercontent.com/ZereBu/Test/main/kpop%20(1).xlsx",
    "Pkmn": "https://raw.githubusercontent.com/ZereBu/Test/main/Pokemon.csv",
    "Data": "https://raw.githubusercontent.com/ZereBu/Test/main/data.csv"
}

# 2️⃣ User selects dataset
selected_csv = st.selectbox("Elige un dataset", list(csv_files.keys()))

# 3️⃣ Load dataset (Excel or CSV)
file_url = csv_files[selected_csv]

try:
    if file_url.endswith(".csv"):
        df = pd.read_csv(file_url)
    else:
        df = pd.read_excel(file_url)

    st.write("### 👀 Vista previa del dataset")
    st.dataframe(df.head())

    # 4️⃣ Pygwalker explorer
    st.write("### 📊 Explorador interactivo")
    renderer = StreamlitRenderer(df)
    renderer.explorer(height=800)

    # 5️⃣ Optional reset button
    if st.button("🔄 Reiniciar explorador"):
        if "pygwalker_state" in st.session_state:
            del st.session_state["pygwalker_state"]
            st.experimental_rerun()

except Exception as e:
    st.error(f"No se pudo cargar el dataset: {e}")
