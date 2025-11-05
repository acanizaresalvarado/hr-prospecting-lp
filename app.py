# Se ejecuta con:
# streamlit run app.py
# Activar .venv con source .venv/bin/activate

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="HR Prospecting & Matching - index", layout="wide")

# Carga el HTML completo
html_code = Path("index.html").read_text(encoding="utf-8")

# Render del HTML
st.components.v1.html(html_code, height=1400, scrolling=True)
