import streamlit as st
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(page_title="Pygwalker Multi-CSV App", layout="wide")
st.title("🔎 Explora tus datos con PyGWalker")

# 1️⃣ List of CSV files in your GitHub repo
csv_files = {
    "Amongus": "https://raw.githubusercontent.com/ZereBu/Test/blob/main/amogus%20(2)%20(1)%20(1).xlsx",
    "Kpop": "https://raw.githubusercontent.comZereBu/Test/blob/main/kpop%20(1).xlsx",
    "Pkmn": "https://raw.githubusercontent.com/ZereBu/Test/blob/main/Pokemon.csv",
    "Data": "https://raw.githubusercontent.com/ZereBu/Test/blob/main/data.csv"
}

# 2️⃣ User selects which CSV to explore
selected_csv = st.selectbox("Elige un dataset", list(csv_files.keys()))

# 3️⃣ Show custom text/questions for each CSV

st.write(custom_texts[selected_csv])

# 4️⃣ Load the selected CSV
df = pd.read_csv(csv_files[selected_csv])

st.write("### 👀 Vista previa del dataset")
st.dataframe(df.head())

# 5️⃣ PyGWalker explorer
st.write("### 📊 Explorador interactivo")
renderer = StreamlitRenderer(df)
renderer.explorer(height=800)

# 6️⃣ Optional reset button
if st.button("🔄 Reiniciar explorador"):
    if "pygwalker_state" in st.session_state:
        del st.session_state["pygwalker_state"]
        st.experimental_rerun()
