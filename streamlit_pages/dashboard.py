import json
import streamlit as st

from app.services.orchestrator import Orchestrator
from app.utils.ui import load_css

# ==========================================================
# PAGE SETUP
# ==========================================================

load_css()

st.title("CodeGuard v3")

st.caption(
    "AI Code Review & Security Analysis Platform"
)

st.divider()

# ==========================================================
# SESSION STATE
# ==========================================================

if "result" not in st.session_state:
    st.session_state["result"] = None

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.subheader("Agents")

    st.write("1. Code Analysis")

    st.write("2. Security")

    st.write("3. Remediation")

    st.write("4. PR Summary")

    st.write("5. AI Assistant")

    st.divider()

    st.subheader("Supported Languages")

    st.write("Python")

    st.write("Java")

    st.divider()

    if st.button(
        "🗑️ Clear Analysis",
        use_container_width=True
    ):

        st.session_state["result"] = None

        st.rerun()

# ==========================================================
# INPUT SECTION
# ==========================================================

left, right = st.columns([1, 2])

with left:

    uploaded_file = st.file_uploader(

        "Upload Python / Java File",

        type=["py", "java"]

    )

    language = st.selectbox(

        "Programming Language",

        [

            "Python",

            "Java"

        ]

    )

    analyze = st.button(

        "🚀 Analyze Code",

        use_container_width=True

    )

with right:

    code = st.text_area(

        "Paste Source Code",

        placeholder="Paste Python or Java source code here...",

        height=420

    )

# ==========================================================
# LOAD FILE
# ==========================================================

filename = "Pasted Code"

if uploaded_file is not None:

    filename = uploaded_file.name

    code = uploaded_file.read().decode("utf-8")

    st.success(f"Loaded : {filename}")

# ==========================================================
# RUN ANALYSIS
# ==========================================================

if analyze:

    if code.strip() == "":

        st.error("Please upload or paste code.")

    else:

        with st.spinner("Running AI Agents..."):

            result = Orchestrator.analyze(

                language=language,

                code=code,

                filename=filename

            )

            st.session_state["result"] = result

        st.success("Analysis Completed Successfully!")

# ==========================================================
# SHOW RESULTS ONLY AFTER ANALYSIS
# ==========================================================

if st.session_state["result"] is not None:

    result = st.session_state["result"]

    project = result["project"]

    code_analysis = result["code_analysis"]

    security = result["security"]

    remediation = result["remediation"]

    summary = result["summary"]

        # ==========================================================
    # PROJECT OVERVIEW
    # ==========================================================

    st.divider()

    st.header("Project Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "Language",

            project["language"]

        )

    with c2:

        st.metric(

            "Filename",

            project["filename"]

        )

    with c3:

        st.metric(

            "Lines of Code",

            project["lines_of_code"]

        )

    with c4:

        st.metric(

            "Health Score",

            f'{summary["health_score"]}/100'

        )

    st.progress(

        summary["health_score"] / 100

    )

    # ==========================================================
    # SECURITY OVERVIEW
    # ==========================================================

    st.divider()

    st.header("🚨 Security Overview")

    s1, s2, s3, s4 = st.columns(4)

    with s1:

        st.error(

            f"🔴 Critical\n\n{security['critical']}"

        )

    with s2:

        st.warning(

            f"🟠 High\n\n{security['high']}"

        )

    with s3:

        st.info(

            f"🟡 Medium\n\n{security['medium']}"

        )

    with s4:

        st.success(

            f"🟢 Low\n\n{security['low']}"

        )

    # ==========================================================
    # AGENT STATISTICS
    # ==========================================================

    st.divider()

    st.header("📈 Agent Statistics")

    a1, a2, a3 = st.columns(3)

    with a1:

        st.metric(

            "Code Findings",

            code_analysis["total_findings"]

        )

    with a2:

        st.metric(

            "Security Findings",

            security["total_findings"]

        )

    with a3:

        st.metric(

            "Issues Fixed",

            remediation["total_issues_fixed"]

        )

    # ==========================================================
    # SOURCE CODE
    # ==========================================================

    st.divider()

    st.header("📄 Uploaded Source Code")

    st.code(

        code,

        language.lower()

    )

    # ==========================================================
    # RESULT TABS
    # ==========================================================

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs(

        [

            "1. Code Analysis",

            "2. Security",

            "3. Remediation",

            "4. PR Summary",

            "5. AI Assistant"

        ]

    )

        # ==========================================================
    # TAB 1 - CODE ANALYSIS
    # ==========================================================

    with tab1:

        st.subheader("📋 Code Analysis Findings")

        if code_analysis["total_findings"] == 0:

            st.success("🎉 No code quality issues detected.")

        else:

            for finding in code_analysis["findings"]:

                severity = finding.get("severity", "Low")

                icon = {
                    "Critical": "🔴",
                    "High": "🟠",
                    "Medium": "🟡",
                    "Low": "🟢"
                }.get(severity, "⚪")

                with st.expander(
                    f"{icon} {finding['title']} ({severity})"
                ):

                    st.write(
                        f"**Description**  \n{finding['description']}"
                    )

                    st.write(
                        f"**Line Number:** {finding['line_number']}"
                    )

                    st.info(
                        finding["suggestion"]
                    )

        st.divider()

        st.subheader("🤖 AI Code Review")

        st.markdown(
            code_analysis["ai_review"]
        )

    # ==========================================================
    # TAB 2 - SECURITY
    # ==========================================================

    with tab2:

        st.subheader("🔒 Security Findings")

        if security["total_findings"] == 0:

            st.success(
                "🎉 No security vulnerabilities detected."
            )

        else:

            for finding in security["findings"]:

                severity = finding.get("severity", "Low")

                icon = {
                    "Critical": "🔴",
                    "High": "🟠",
                    "Medium": "🟡",
                    "Low": "🟢"
                }.get(severity, "⚪")

                with st.expander(
                    f"{icon} {finding['title']} ({severity})"
                ):

                    st.write(
                        f"**Description**  \n{finding['description']}"
                    )

                    st.write(
                        f"**Line Number:** {finding['line_number']}"
                    )

                    st.warning(
                        finding["suggestion"]
                    )

        st.divider()

        st.subheader("🛡️ AI Security Review")

        st.markdown(
            security["ai_review"]
        )

    # ==========================================================
    # TAB 3 - REMEDIATION
    # ==========================================================

    with tab3:

        st.subheader("🛠 AI Remediation")

        st.markdown(
            remediation["result"]
        )

    # ==========================================================
    # TAB 4 - SUMMARY
    # ==========================================================

    with tab4:

        st.subheader("📄 Pull Request Summary")

        st.markdown(
            summary["summary"]
        )

    # ==========================================================
    # TAB 5 - AI ASSISTANT
    # ==========================================================

    with tab5:

        st.subheader("💬 Ask CodeGuard")

        question = st.text_input(

            "Ask about secure coding, OWASP, Python or Java"

        )

        if st.button(
            "Ask Assistant",
            key="assistant_btn"
        ):

            if question.strip():

                from app.agents.assistant_agent import AssistantAgent

                response = AssistantAgent.ask(question)

                if response["status"] == "success":

                    st.success("Answer")

                    st.markdown(
                        response["answer"]
                    )

                else:

                    st.error(
                        response["message"]
                    )

                        # ==========================================================
    # EXPORT REPORTS
    # ==========================================================

    st.divider()

    st.header("📥 Export Reports")

    json_report = json.dumps(
        result,
        indent=4
    )

    markdown_report = f"""
# CodeGuard v3 Report

## Project

Filename : {project["filename"]}

Language : {project["language"]}

Lines : {project["lines_of_code"]}

Health Score : {summary["health_score"]}

---

## Code Findings

Total : {code_analysis["total_findings"]}

---

## Security Findings

Critical : {security["critical"]}

High : {security["high"]}

Medium : {security["medium"]}

Low : {security["low"]}

---

## Pull Request Summary

{summary["summary"]}

---

Generated by CodeGuard v3
"""

    d1, d2 = st.columns(2)

    with d1:

        st.download_button(

            label="⬇ Download JSON",

            data=json_report,

            file_name="codeguard_report.json",

            mime="application/json",

            use_container_width=True

        )

    with d2:

        st.download_button(

            label="⬇ Download Markdown",

            data=markdown_report,

            file_name="codeguard_report.md",

            mime="text/markdown",

            use_container_width=True

        )

    # ==========================================================
    # RAW JSON (OPTIONAL)
    # ==========================================================

    with st.expander("🔍 View Raw JSON Report"):

        st.json(result)

    # ==========================================================
    # ANALYSIS SUMMARY
    # ==========================================================

    st.divider()

    st.header("📈 Analysis Summary")

    total_findings = (
        code_analysis["total_findings"]
        + security["total_findings"]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Findings",
            total_findings
        )

    with col2:

        st.metric(
            "Code Issues",
            code_analysis["total_findings"]
        )

    with col3:

        st.metric(
            "Security Issues",
            security["total_findings"]
        )

    # ==========================================================
    # CLEAR RESULTS
    # ==========================================================

    st.divider()

    if st.button(
        "🗑 Clear Analysis Results",
        use_container_width=True
    ):

        st.session_state["result"] = None

        st.rerun()

    # ==========================================================
    # FOOTER
    # ==========================================================

    st.divider()

    st.caption(
        """
         **CodeGuard v3**

AI Code Review & Security Analysis Platform

Powered by:

- 🚀 Groq LLM
- 🧠 ChromaDB
- 🐘 PostgreSQL
- ⚡ Streamlit

Version 1.0.0
"""
    )