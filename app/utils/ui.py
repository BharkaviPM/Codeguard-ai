# app/utils/ui.py

from pathlib import Path
import streamlit as st


def load_css():

    css = Path("assets/style.css")

    if css.exists():

        with open(css) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )