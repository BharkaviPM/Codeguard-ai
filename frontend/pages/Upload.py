import os
import time
import tempfile

import streamlit as st

from components.api import upload_project
from utils.helpers import initialize_session

initialize_session()

st.set_page_config(
    page_title="CodeGuard AI",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ CodeGuard AI")
st.caption("AI Powered Secure Code Review Platform")

st.divider()

uploaded_file = st.file_uploader(
    "Upload Python / Java Source File",
    type=["py", "java", "zip"],
)

if uploaded_file:

    st.success(f"Selected : {uploaded_file.name}")

    if st.button(
        "🚀 Analyze Code",
        use_container_width=True,
    ):

        try:

            progress = st.progress(0)
            status = st.empty()

            # --------------------------------------------------
            # Save uploaded file locally for frontend analysis
            # --------------------------------------------------

            status.info("Preparing project...")

            suffix = os.path.splitext(uploaded_file.name)[1]

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix,
            ) as tmp:

                tmp.write(uploaded_file.getbuffer())

                temp_path = tmp.name

            st.session_state.project_path = temp_path
            st.session_state.file_name = uploaded_file.name

            progress.progress(20)

            # --------------------------------------------------
            # Upload to backend (optional)
            # --------------------------------------------------

            status.info("Uploading project...")

            upload_response = upload_project(uploaded_file)

            progress.progress(40)

            time.sleep(0.5)

            status.info("Running Code Analysis...")

            progress.progress(60)

            time.sleep(0.5)

            status.info("Preparing Dashboard...")

            progress.progress(80)

            time.sleep(0.5)

            progress.progress(100)

            st.success("Analysis Completed Successfully ✅")

            st.session_state.project_id = upload_response.get(
                "project_id",
                None,
            )

            st.session_state.project_name = upload_response.get(
                "project_name",
                uploaded_file.name,
            )

            st.switch_page("pages/Results.py")

        except Exception as e:

            st.error(f"Error: {e}")