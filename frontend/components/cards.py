import streamlit as st


def summary_cards(summary):

    st.subheader("📊 Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Critical",
            summary.get("critical", 0),
        )

        st.metric(
            "High",
            summary.get("high", 0),
        )

    with c2:

        st.metric(
            "Medium",
            summary.get("medium", 0),
        )

        st.metric(
            "Low",
            summary.get("low", 0),
        )

    with c3:

        st.metric(
            "Files",
            summary.get("files", 0),
        )

        st.metric(
            "LOC",
            summary.get("loc", 0),
        )

    with c4:

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