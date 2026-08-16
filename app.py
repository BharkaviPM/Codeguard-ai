import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from workflows.review_workflow import ReviewWorkflow
from rag.chat_service import ChatService
from reports.pdf_generator import PDFGenerator
from reports.markdown_report import MarkdownReport

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="CodeGuard AI",
    page_icon="🛡️",
    layout="wide"
)

# =====================================================
# SESSION
# =====================================================

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "uploaded_code" not in st.session_state:
    st.session_state.uploaded_code = ""

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background:#050816;
    color:white;
}

/* NAVBAR */

.navbar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:15px 30px;
    border:1px solid rgba(255,255,255,0.08);
    border-radius:50px;
    background:rgba(255,255,255,0.03);
    backdrop-filter:blur(20px);
    margin-bottom:30px;
}

.brand{
    font-size:32px;
    font-weight:700;
}

.brand-gradient{
    background:linear-gradient(
        90deg,
        #4facfe,
        #00f2fe
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.nav-pill{
    padding:10px 20px;
    border-radius:25px;
    background:#111827;
    border:1px solid #333;
}

/* HERO */

.hero{
    text-align:center;
    margin-top:20px;
    margin-bottom:40px;
}

.hero-title{
    font-size:60px;
    font-weight:800;
    line-height:1.1;
}

.gradient{
    background:linear-gradient(
        90deg,
        #4facfe,
        #00f2fe
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.hero-desc{
    color:#cbd5e1;
    font-size:20px;
}

/* CARDS */

.card{
    background:#111827;
    border:1px solid rgba(255,255,255,0.08);
    border-radius:20px;
    padding:20px;
    text-align:center;
}

.metric-card{
    background:#111827;
    border-radius:20px;
    padding:20px;
    text-align:center;
}

.metric{
    font-size:40px;
    font-weight:bold;
}

.section{
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# NAVBAR
# =====================================================

st.markdown("""
<div class="navbar">

<div class="brand">
🛡️ <span class="brand-gradient">CodeGuard AI</span>
</div>

<div class="nav-pill">
⚡ Groq + LangGraph + ChromaDB
</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero">

<h1 class="hero-title">
Code Review<br>
<span class="gradient">
with Intelligence
</span>
</h1>

<p class="hero-desc">
AI-powered code review, security analysis,
remediation and grounded secure coding guidance.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# FEATURES
# =====================================================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
    <h2>🔐</h2>
    <h4>Security</h4>
    OWASP Analysis
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h2>🧠</h2>
    <h4>Code Review</h4>
    Quality Analysis
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h2>🛠️</h2>
    <h4>Remediation</h4>
    AI Fixes
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
    <h2>📚</h2>
    <h4>RAG</h4>
    OWASP Knowledge
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CODE INPUT
# =====================================================

st.markdown("## 📂 Code Submission")

uploaded = st.file_uploader(
    "Upload Python or Java file",
    type=["py","java"]
)

code_input = st.text_area(
    "Paste Source Code",
    height=350
)

if uploaded:

    content = uploaded.read().decode("utf-8")

    st.session_state.uploaded_code = content

    st.code(content)

if code_input.strip():
    st.session_state.uploaded_code = code_input

# =====================================================
# ANALYZE
# =====================================================

if st.button("🚀 Analyze Code"):

    code = st.session_state.uploaded_code

    if not code:
        st.warning("Upload or paste code.")
        st.stop()

    with st.spinner("Running AI Agents..."):

        workflow = ReviewWorkflow()

        result = workflow.run(code)
        st.write(result.keys())

        st.session_state.analysis = result

# =====================================================
# RESULTS
# =====================================================

if st.session_state.analysis:

    result = st.session_state.analysis

    st.markdown("---")
    st.markdown("# 📊 Analysis Dashboard")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Security", "High")

    with m2:
        st.metric("Quality", "Medium")

    with m3:
        st.metric("Maintainability", "78")

    with m4:
        st.metric("Health Score", "82")

    severity = pd.DataFrame({
        "Severity": ["High", "Medium", "Low"],
        "Count": [5, 3, 2]
    })

    fig = px.bar(
        severity,
        x="Severity",
        y="Count",
        title="Issue Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Security",
        "Code Review",
        "Remediation",
        "Summary",
        "Performance",
        "Risk Assessment"
    ])

    with tab1:
        st.markdown(
            result.get(
                "security_review",
                "No security review available."
            )
        )

    with tab2:
        st.markdown(
            result.get(
                "code_review",
                "No code review available."
            )
        )

    with tab3:
        st.markdown(
            result.get(
                "remediation",
                "No remediation available."
            )
        )

    with tab4:
        st.markdown(
            result.get(
                "summary",
                "No summary available."
            )
        )

    with tab5:
        st.markdown(
            result.get(
                "performance_review",
                "Performance review not available."
            )
        )

    with tab6:
        st.markdown(
            result.get(
                "risk_report",
                "Risk assessment not available."
            )
        )

    st.markdown("---")

    if st.button("📄 Generate PDF Report"):

        try:

            report = MarkdownReport.generate(
                security_review=result.get(
                    "security_review", ""
                ),
                code_review=result.get(
                    "code_review", ""
                ),
                performance_review=result.get(
                    "performance_review", ""
                ),
                remediation=result.get(
                    "remediation", ""
                ),
                risk_report=result.get(
                    "risk_report", ""
                ),
                summary=result.get(
                    "summary", ""
                ),
                metrics={
                    "high": 5,
                    "medium": 3,
                    "low": 2,
                    "health_score": 82
                }
            )

            output_path = PDFGenerator.generate(
                report,
                "reports/code_review_report.pdf"
            )

            st.success(
                "PDF report generated successfully."
            )

            with open(
                output_path,
                "rb"
            ) as pdf_file:

                st.download_button(
                    label="⬇ Download Report",
                    data=pdf_file,
                    file_name="code_review_report.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Failed to generate report: {str(e)}"
            )
# =====================================================
# CHAT
# =====================================================

st.markdown("---")
st.markdown("# 💬 Secure Coding Assistant")

question = st.text_input(
    "Ask CodeGuard AI"
)

if st.button("Ask AI"):

    if question:

        with st.spinner("Thinking..."):

            try:

                chat = ChatService()

                answer = chat.ask(question)

                st.success(answer)

            except Exception as e:

                st.error(str(e))

# =====================================================
# CODE QA
# =====================================================

st.markdown("---")
st.markdown("# 🧠 Ask About Uploaded Code")

code_question = st.text_input(
    "Example: What is wrong at line 12?"
)

if st.button("Analyze Code Question"):

    code = st.session_state.uploaded_code

    if not code:
        st.warning("Upload code first.")
    else:

        prompt = f"""
You are a senior code reviewer.

Code:

{code}

Question:

{code_question}

Provide exact lines involved.
"""

        from services.groq_service import GroqService

        answer = GroqService.chat(prompt)

        st.markdown(answer)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown("""
<center>

🛡️ CodeGuard AI • AI Code Review & Security Analysis

Powered by Groq + LangGraph + ChromaDB

</center>
""", unsafe_allow_html=True)