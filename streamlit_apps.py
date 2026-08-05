import streamlit as st
import json

from app.services.orchestrator import Orchestrator
from app.agents.assistant_agent import AssistantAgent


# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="CodeGuard v3",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main{
    background:#0F172A;
}

.block-container{
    padding-top:1.5rem;
}

h1,h2,h3{
    color:white;
}

.stTextArea textarea{
    font-family:Consolas;
    font-size:14px;
}

.metric-card{
    background:#1E293B;
    padding:15px;
    border-radius:12px;
}

div[data-testid="metric-container"]{
    background:#1E293B;
    border:1px solid #334155;
    padding:15px;
    border-radius:12px;
}

div[data-testid="stExpander"]{
    border-radius:10px;
    border:1px solid #334155;
}

.stButton button{
    width:100%;
    height:45px;
    border-radius:10px;
    font-weight:bold;
    background:#4F46E5;
    color:white;
}

.stDownloadButton button{
    width:100%;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.title("🛡️ CodeGuard v3")

    st.caption(
        "AI Code Review & Security Analysis Agent"
    )

    st.divider()

    st.write("### Supported Languages")

    st.success("✔ Python")

    st.success("✔ Java")

    st.divider()

    st.write("### AI Agents")

    st.write("✅ Code Analysis")

    st.write("✅ Security")

    st.write("✅ Remediation")

    st.write("✅ PR Summary")

    st.write("✅ Assistant")


# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("🛡️ CodeGuard v3")

st.caption(
    "AI Powered Code Review, Security Analysis & Secure Coding Assistant"
)

st.divider()


# ---------------------------------------------------
# Upload Section
# ---------------------------------------------------

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

        "🚀 Analyze Code"

    )


with right:

    code = st.text_area(

        "Paste Source Code",

        height=420,

        placeholder="Paste Python or Java source code here..."

    )


# ---------------------------------------------------
# Read Uploaded File
# ---------------------------------------------------

if uploaded_file:

    code = uploaded_file.read().decode()

    st.success(

        f"Loaded : {uploaded_file.name}"

    )


# ---------------------------------------------------
# Analyze
# ---------------------------------------------------

if analyze:

    if code.strip() == "":

        st.error(

            "Please upload or paste source code."

        )

        st.stop()

    with st.spinner(

        "Running AI Agents..."

    ):

        result = Orchestrator.analyze(

            language=language,

            code=code,

            filename=uploaded_file.name if uploaded_file else "Pasted Code"

        )

        st.session_state["result"] = result

    st.success(

        "Analysis Completed Successfully!"

    )

    # ==========================================================
# RESULTS DASHBOARD
# ==========================================================

if "result" in st.session_state:

    result = st.session_state["result"]

    project = result["project"]

    summary = result["summary"]

    security = result["security"]

    code_agent = result["code_agent"]

    st.divider()

    st.header("📊 Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(

            "Language",

            project["language"]

        )

    with col2:

        st.metric(

            "File",

            project["filename"]

        )

    with col3:

        st.metric(

            "Lines of Code",

            project["lines_of_code"]

        )

    with col4:

        st.metric(

            "Health Score",

            f'{summary["health_score"]}/100'

        )

    st.divider()

    st.header("🚨 Security Severity")

    s1, s2, s3, s4 = st.columns(4)

    s1.metric(

        "Critical",

        security["critical"]

    )

    s2.metric(

        "High",

        security["high"]

    )

    s3.metric(

        "Medium",

        security["medium"]

    )

    s4.metric(

        "Low",

        security["low"]

    )

    st.divider()

    st.header("📈 Agent Statistics")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "Code Findings",

            code_agent["total_findings"]

        )

    with c2:

        st.metric(

            "Security Findings",

            security["total_findings"]

        )

    with c3:

        st.metric(

            "Issues Fixed",

            result["remediation"]["total_issues_fixed"]

        )

        # ==========================================================
# CODE ANALYSIS FINDINGS
# ==========================================================

st.divider()

st.header("📋 Code Analysis Findings")

if code_agent["total_findings"] == 0:

    st.success("🎉 No code quality issues detected.")

else:

    for finding in code_agent["findings"]:

        severity = finding["severity"]

        icon = {
            "Critical": "🔴",
            "High": "🟠",
            "Medium": "🟡",
            "Low": "🟢"
        }.get(severity, "⚪")

        with st.expander(
            f'{icon} {finding["title"]} ({severity})'
        ):

            st.write("### Description")

            st.write(
                finding["description"]
            )

            st.write("### Line")

            st.code(
                str(finding["line_number"])
            )

            st.write("### Recommendation")

            st.info(
                finding["suggestion"]
            )


# ==========================================================
# SECURITY FINDINGS
# ==========================================================

st.divider()

st.header("🔒 Security Findings")

if security["total_findings"] == 0:

    st.success("🎉 No security vulnerabilities detected.")

else:

    for finding in security["findings"]:

        severity = finding["severity"]

        icon = {
            "Critical": "🔴",
            "High": "🟠",
            "Medium": "🟡",
            "Low": "🟢"
        }.get(severity, "⚪")

        with st.expander(
            f'{icon} {finding["title"]} ({severity})'
        ):

            st.write("### Description")

            st.write(
                finding["description"]
            )

            st.write("### Line")

            st.code(
                str(finding["line_number"])
            )

            st.write("### Recommendation")

            st.warning(
                finding["suggestion"]
            )


# ==========================================================
# AI CODE REVIEW
# ==========================================================

st.divider()

st.header("🤖 AI Code Review")

with st.expander("View AI Code Review", expanded=True):

    st.markdown(

        code_agent["ai_review"]

    )


# ==========================================================
# AI SECURITY REVIEW
# ==========================================================

st.divider()

st.header("🛡️ AI Security Review")

with st.expander("View AI Security Review", expanded=True):

    st.markdown(

        security["ai_review"]

    )

    # ==========================================================
# AI REMEDIATION
# ==========================================================

st.divider()

st.header("🛠 AI Remediation")

with st.expander("View Complete Remediation", expanded=True):

    st.markdown(

        result["remediation"]["result"]

    )


# ==========================================================
# PR SUMMARY
# ==========================================================

st.divider()

st.header("📄 Pull Request Summary")

with st.expander("View PR Summary", expanded=True):

    st.markdown(

        result["summary"]["summary"]

    )


# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

st.divider()

st.header("📥 Export Report")

report_json = json.dumps(

    result,

    indent=4

)

col1, col2 = st.columns(2)

with col1:

    st.download_button(

        "⬇ Download JSON",

        report_json,

        file_name="codeguard_report.json",

        mime="application/json"

    )

with col2:

    st.download_button(

        "⬇ Download Markdown",

        result["summary"]["summary"],

        file_name="codeguard_summary.md",

        mime="text/markdown"

    )


# ==========================================================
# AI ASSISTANT
# ==========================================================

st.divider()

st.header("💬 Ask CodeGuard")

question = st.text_input(

    "Ask a security or coding question"

)

if st.button("Ask Assistant"):

    if question.strip():

        with st.spinner("Thinking..."):

            answer = AssistantAgent.ask(question)

            st.markdown(answer["answer"])


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "🛡️ CodeGuard v3 | AI Code Review & Security Analysis Platform | Powered by Groq + ChromaDB + Streamlit"
)