import pandas as pd
import streamlit as st


def dataframe(title, data):

    st.subheader(title)

    if not data:

        st.info("No data available.")

        return

    df = pd.DataFrame(data)

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True,

    )


def findings(findings):

    dataframe(

        "🔍 Findings",

        findings,

    )


def security(security):

    dataframe(

        "🔒 Security",

        security,

    )


def metrics(metrics):

    dataframe(

        "📈 Metrics",

        metrics,

    )


def complexity(complexity):

    dataframe(

        "📐 Complexity",

        complexity,

    )