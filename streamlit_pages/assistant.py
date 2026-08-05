import streamlit as st
from app.utils.ui import load_css

load_css()

from app.agents.assistant_agent import AssistantAgent


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.title("💬 AI Code Assistant")

st.caption(
    "Ask questions about OWASP, Secure Coding, Python, Java, and vulnerabilities."
)

st.divider()


# ==========================================================
# SESSION STATE
# ==========================================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("Assistant")

    st.write(
        """
This assistant uses

- ChromaDB
- RAG
- Groq LLM

to answer secure coding questions.
"""
    )

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.chat_history = []

        st.rerun()


# ==========================================================
# EXAMPLE QUESTIONS
# ==========================================================

st.subheader("Example Questions")

c1, c2 = st.columns(2)

with c1:

    if st.button("How to prevent SQL Injection?"):

        st.session_state.question = (
            "How to prevent SQL Injection?"
        )

with c2:

    if st.button("Explain XSS Prevention"):

        st.session_state.question = (
            "Explain XSS Prevention."
        )

c3, c4 = st.columns(2)

with c3:

    if st.button("Python Secure Coding"):

        st.session_state.question = (
            "Explain Python Secure Coding."
        )

with c4:

    if st.button("Java Best Practices"):

        st.session_state.question = (
            "Explain Java Secure Coding Best Practices."
        )


# ==========================================================
# QUESTION INPUT
# ==========================================================

question = st.text_area(

    "Ask anything",

    value=st.session_state.get("question", ""),

    height=120,

    placeholder="Example: What is SQL Injection?"

)


# ==========================================================
# ASK BUTTON
# ==========================================================

if st.button(

    "🚀 Ask Assistant",

    use_container_width=True

):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            response = AssistantAgent.ask(question)

        if response["status"] == "success":

            st.session_state.chat_history.append(

                {

                    "question": question,

                    "answer": response["answer"]

                }

            )

            st.session_state.question = ""

            st.rerun()

        else:

            st.error(response["message"])


# ==========================================================
# CHAT HISTORY
# ==========================================================

st.divider()

st.header("Conversation")

if len(st.session_state.chat_history) == 0:

    st.info("No conversation yet.")

else:

    for chat in reversed(

        st.session_state.chat_history

    ):

        with st.chat_message("user"):

            st.markdown(

                chat["question"]

            )

        with st.chat_message("assistant"):

            st.markdown(

                chat["answer"]

            )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(

    "CodeGuard v3 AI Assistant | Powered by RAG + ChromaDB + Groq"

)