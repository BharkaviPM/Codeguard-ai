import streamlit as st

from components.api import ask_chat

st.set_page_config(

    page_title="AI Chat",

    page_icon="💬",

    layout="wide",

)

st.title("💬 CodeGuard AI Assistant")

if "messages" not in st.session_state:

    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(

        message["role"]

    ):

        st.write(

            message["content"]

        )

prompt = st.chat_input(

    "Ask about your project..."

)

if prompt:

    st.session_state.messages.append(

        {

            "role": "user",

            "content": prompt,

        }

    )

    with st.chat_message("user"):

        st.write(prompt)

    try:

        project_id = st.session_state.get(

            "project_id"

        )

        response = ask_chat(

            prompt,

            project_id,

        )

        answer = response.get(

            "answer",

            "No response.",

        )

    except Exception as ex:

        answer = str(ex)

    with st.chat_message(

        "assistant"

    ):

        st.write(answer)

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": answer,

        }

    )