import streamlit as st

from utils.helpers import initialize_session

initialize_session()

st.set_page_config(

    page_title="CodeGuard AI",

    page_icon="🛡️",

    layout="wide",

)

st.title("🛡️ CodeGuard AI")

st.caption(

    "AI Powered Static Code Analysis Platform"

)

st.divider()

st.markdown("""

## Features

- 📂 Upload ZIP Projects

- 🔍 AST Analysis

- 📈 Radon Metrics

- 🧹 Flake8

- 📝 Pylint

- 🔒 Bandit

- ⚡ Semgrep

- 🤖 AI Summary

- 💬 AI Chat Assistant

- 📄 Report Generation

---

""")

with st.sidebar:

    st.title("🛡 CodeGuard AI")