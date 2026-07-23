import json

import streamlit as st

from components.api import (
    get_results,
    get_summary,
)

st.set_page_config(

    page_title="Analysis Report",

    page_icon="📄",

    layout="wide",

)

st.title("📄 CodeGuard Report")

if "project_id" not in st.session_state:

    st.warning(
        "Upload a project first."
    )

    st.stop()

project_id = st.session_state.project_id

try:

    summary = get_summary(project_id)

    results = get_results(project_id)

except Exception as ex:

    st.error(str(ex))

    st.stop()

st.header("Executive Summary")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Files",
        summary.get("files", 0),
    )

    st.metric(
        "Critical",
        summary.get("critical", 0),
    )

    st.metric(
        "High",
        summary.get("high", 0),
    )

    st.metric(
        "Medium",
        summary.get("medium", 0),
    )

with col2:

    st.metric(
        "Low",
        summary.get("low", 0),
    )

    st.metric(
        "LOC",
        summary.get("loc", 0),
    )

    st.metric(
        "Avg Complexity",
        summary.get(
            "avg_complexity",
            0,
        ),
    )

    st.metric(
        "Maintainability",
        summary.get(
            "maintainability",
            0,
        ),
    )

st.divider()

st.subheader("🤖 AI Summary")

st.write(

    results.get(

        "ai_summary",

        "AI Summary unavailable."

    )

)

st.divider()

st.download_button(

    label="⬇ Download JSON Report",

    data=json.dumps(

        {

            "summary": summary,

            "results": results,

        },

        indent=4,

    ),

    file_name="codeguard_report.json",

    mime="application/json",

)