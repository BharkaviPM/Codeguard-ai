import streamlit as st

st.set_page_config(
    page_title="CodeGuard v3",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Redirect users to the Dashboard page
dashboard = st.Page(
    "streamlit_pages/dashboard.py",
    title="Dashboard",
    icon="🏠",
    default=True
)

assistant = st.Page(
    "streamlit_pages/assistant.py",
    title="AI Assistant",
    icon="💬"
)

reports = st.Page(
    "streamlit_pages/reports.py",
    title="Reports",
    icon="📄"
)

about = st.Page(
    "streamlit_pages/about.py",
    title="About",
    icon="ℹ️"
)

pg = st.navigation([
    dashboard,
    assistant,
    reports,
    about
])

pg.run()