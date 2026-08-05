import streamlit as st
from app.utils.ui import load_css

load_css()

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.title("ℹ️ About CodeGuard v3")

st.caption(
    "AI Code Review & Security Analysis Platform"
)

st.divider()

# ==========================================================
# PROJECT
# ==========================================================

st.header("🛡️ Project Overview")

st.markdown("""
**CodeGuard v3** is an AI-powered code review platform that automatically analyzes Python and Java source code for:

- Code Quality Issues
- Security Vulnerabilities
- OWASP Top 10 Risks
- Secure Coding Best Practices
- AI-based Remediation
- Pull Request Style Review
- Conversational Secure Coding Assistant

The platform combines traditional static analysis with Large Language Models (Groq) and Retrieval-Augmented Generation (RAG) to provide intelligent, explainable, and actionable code reviews.
""")

st.divider()

# ==========================================================
# SYSTEM ARCHITECTURE
# ==========================================================

st.header("🏗️ System Architecture")

st.code("""
                Streamlit Dashboard
                        │
                        ▼
               Multi-Agent Orchestrator
                        │
        ┌────────┬────────┬────────┬────────┐
        ▼        ▼        ▼        ▼
   Code Agent  Security  Remediation Summary
                        │
                        ▼
               Conversational Assistant
                        │
                        ▼
               RAG + ChromaDB
                        │
                        ▼
                     Groq API
""")

st.divider()

# ==========================================================
# AI AGENTS
# ==========================================================

st.header("🤖 AI Agents")

agents = [
    (
        "📋 Code Analysis Agent",
        "Detects code smells, poor coding practices, missing documentation, and maintainability issues."
    ),
    (
        "🔒 Security Agent",
        "Scans for OWASP Top 10 vulnerabilities such as SQL Injection, XSS, hardcoded secrets, unsafe eval(), command injection, and path traversal."
    ),
    (
        "🛠️ Remediation Agent",
        "Uses Groq LLM to generate secure code fixes and detailed explanations."
    ),
    (
        "📄 PR Summary Agent",
        "Creates a pull-request style review with executive summary, security overview, and recommendations."
    ),
    (
        "💬 Assistant Agent",
        "Answers secure coding questions using RAG with ChromaDB and the indexed knowledge base."
    )
]

for title, desc in agents:
    with st.expander(title):
        st.write(desc)

st.divider()

# ==========================================================
# MODULES
# ==========================================================

st.header("📦 Modules")

modules = [
    "Code Submission Module",
    "Secure Coding Knowledge Base",
    "RAG Pipeline",
    "Code Analysis",
    "Security Analysis",
    "Remediation",
    "Pull Request Summary",
    "Conversational Assistant",
    "Report Generation"
]

for module in modules:
    st.success(module)

st.divider()

# ==========================================================
# TECH STACK
# ==========================================================

st.header("🛠️ Tech Stack")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### Backend
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

### AI
- Groq API
- ChromaDB
- Sentence Transformers
- LangChain
""")

with col2:
    st.markdown("""
### Frontend
- Streamlit

### Knowledge Base
- OWASP
- CERT Secure Coding
- CWE
- Python Secure Coding
- Java Secure Coding
""")

st.divider()

# ==========================================================
# FEATURES
# ==========================================================

st.header("⭐ Features")

features = [
    "Python & Java Code Review",
    "AI Code Analysis",
    "OWASP Security Scanning",
    "Severity Scoring",
    "Health Score",
    "AI Remediation",
    "Pull Request Summary",
    "Conversational Assistant",
    "Knowledge Base Search",
    "JSON Report Export",
    "Markdown Report Export"
]

for feature in features:
    st.checkbox(feature, value=True, disabled=True)

st.divider()

# ==========================================================
# PROJECT WORKFLOW
# ==========================================================

st.header("🔄 Workflow")

st.code("""
Upload Source Code
        │
        ▼
Language Detection
        │
        ▼
Multi-Agent Analysis
        │
        ├──────────────► Code Analysis
        │
        ├──────────────► Security Analysis
        │
        ├──────────────► AI Remediation
        │
        └──────────────► PR Summary
                        │
                        ▼
                Dashboard Results
                        │
                        ▼
               Ask AI Assistant
""")

st.divider()

# ==========================================================
# DATABASE
# ==========================================================

st.header("🗄️ Storage")

st.info("""
**PostgreSQL**

Stores:

- Project metadata
- Uploaded files
- Analysis history
- Reports

**ChromaDB**

Stores:

- OWASP Knowledge Base
- CERT Secure Coding
- CWE Documents
- Python Secure Coding
- Java Secure Coding
""")

st.divider()

# ==========================================================
# VERSION
# ==========================================================

st.header("📌 Version")

st.write("**Project Name:** CodeGuard v3")
st.write("**Version:** 1.0.0")
st.write("**Status:** Completed")
st.write("**Architecture:** Multi-Agent AI Platform")

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "🛡️ CodeGuard v3 | AI Code Review & Security Analysis Platform | Powered by Groq • ChromaDB • PostgreSQL • Streamlit"
)