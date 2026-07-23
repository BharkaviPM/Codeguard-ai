import streamlit as st


def initialize_session():

    defaults = {

        "project_id": None,

        "project_name": None,

        "analysis_complete": False,

        "results": None,

        "summary": None,

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


def clear_session():

    keys = list(st.session_state.keys())

    for key in keys:

        del st.session_state[key]


def analysis_available():

    return (

        st.session_state.project_id is not None

        and

        st.session_state.analysis_complete

    )