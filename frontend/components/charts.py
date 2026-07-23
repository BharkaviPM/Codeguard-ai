import pandas as pd
import plotly.express as px
import streamlit as st


def severity_chart(summary):

    data = pd.DataFrame({

        "Severity": [

            "Critical",

            "High",

            "Medium",

            "Low",

        ],

        "Count": [

            summary.get("critical", 0),

            summary.get("high", 0),

            summary.get("medium", 0),

            summary.get("low", 0),

        ],

    })

    fig = px.pie(

        data,

        names="Severity",

        values="Count",

        title="Issue Severity",

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


def complexity_chart(complexity):

    if not complexity:

        return

    df = pd.DataFrame(complexity)

    if "complexity" not in df.columns:

        return

    fig = px.histogram(

        df,

        x="complexity",

        title="Complexity Distribution",

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )


def maintainability_chart(metrics):

    if not metrics:

        return

    df = pd.DataFrame(metrics)

    if "maintainability" not in df.columns:

        return

    fig = px.bar(

        df,

        x="file",

        y="maintainability",

        title="Maintainability Index",

    )

    st.plotly_chart(

        fig,

        use_container_width=True,

    )