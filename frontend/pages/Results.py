import streamlit as st

from ai.analyzer import analyze_project

from components.table import (
    findings,
    metrics,
    security,
    complexity,
)

from components.charts import (
    severity_chart,
    complexity_chart,
    maintainability_chart,
)

from utils.helpers import initialize_session

initialize_session()

st.set_page_config(
    page_title="Analysis Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 CodeGuard AI Dashboard")

st.caption(
    "AI Powered Static Code Analysis"
)

project_path = st.session_state.get(
    "project_path"
)

project_name = st.session_state.get(
    "file_name",
    "Unknown Project",
)

if project_path is None:

    st.warning(
        "Please upload a project first."
    )

    st.stop()

# ----------------------------------------------------
# Run AI Analysis
# ----------------------------------------------------

try:

    with st.spinner(
        "Analyzing source code..."
    ):

        results = analyze_project(
            project_path
        )

        summary = results["summary"]

except Exception as ex:

    st.exception(ex)

    st.stop()

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.success(
    f"Analysis completed : **{project_name}**"
)

st.divider()

# ----------------------------------------------------
# KPI Cards
# ----------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Health Score",
    f'{summary["health_score"]}/100'
)

c2.metric(
    "Security Issues",
    summary["security"]
)

c3.metric(
    "Code Findings",
    summary["quality"]
)

c4.metric(
    "Maintainability",
    summary["maintainability"]
)

st.progress(
    summary["health_score"] / 100
)

if summary["health_score"] >= 90:

    st.success(
        "🟢 Excellent Code Quality"
    )

elif summary["health_score"] >= 75:

    st.info(
        "🟡 Good Code Quality"
    )

elif summary["health_score"] >= 60:

    st.warning(
        "🟠 Needs Improvement"
    )

else:

    st.error(
        "🔴 Critical Project"
    )

    # ----------------------------------------------------
# Charts
# ----------------------------------------------------

st.divider()

st.subheader("📈 Code Analysis Overview")

col1, col2 = st.columns(2)

# --------------------------------------------
# Severity Chart
# --------------------------------------------

with col1:

    st.markdown("### 🚨 Severity Distribution")

    try:

        severity_chart(summary)

    except Exception:

        severity_data = {
            "Critical": summary["critical"],
            "High": summary["high"],
            "Medium": summary["medium"],
            "Low": summary["low"],
        }

        st.bar_chart(severity_data)

# --------------------------------------------
# Maintainability
# --------------------------------------------

with col2:

    st.markdown("### 🛠 Maintainability")

    try:

        maintainability_chart(
            results["metrics"]
        )

    except Exception:

        maintainability = summary["maintainability"]

        st.metric(
            "Maintainability Score",
            f"{maintainability}/100",
        )

        st.progress(
            maintainability / 100
        )

# ----------------------------------------------------
# Complexity
# ----------------------------------------------------

st.divider()

st.subheader("📊 Cyclomatic Complexity")

try:

    complexity_chart(
        results["complexity"]
    )

except Exception:

    complexity_data = {
        item["function"]: item["complexity"]
        for item in results["complexity"]
    }

    if complexity_data:

        st.bar_chart(complexity_data)

    else:

        st.info(
            "No complexity information available."
        )

# ----------------------------------------------------
# AI Summary
# ----------------------------------------------------

st.divider()

st.subheader("🤖 AI Code Review")

health = summary["health_score"]

if health >= 90:

    color = "🟢 Excellent"

elif health >= 75:

    color = "🟡 Good"

elif health >= 60:

    color = "🟠 Fair"

else:

    color = "🔴 Poor"

st.success(f"""
### Overall Code Health : {color}

**Health Score:** {summary["health_score"]}/100

**Maintainability:** {summary["maintainability"]}/100

**Security Issues:** {summary["security"]}

**Quality Findings:** {summary["quality"]}

---

### 🤖 AI Summary

{results["ai_summary"]}
""")

# ----------------------------------------------------
# Recommendations
# ----------------------------------------------------

st.subheader("💡 Recommendations")

recommendations = []

if summary["critical"] > 0:

    recommendations.append(
        "Immediately fix all CRITICAL security issues."
    )

if summary["high"] > 0:

    recommendations.append(
        "Resolve HIGH severity vulnerabilities before deployment."
    )

if summary["maintainability"] < 70:

    recommendations.append(
        "Refactor complex functions to improve maintainability."
    )

if summary["quality"] > 10:

    recommendations.append(
        "Reduce code smells and improve readability."
    )

if not recommendations:

    recommendations.append(
        "Great job! No major improvements are currently recommended."
    )

for rec in recommendations:

    st.info(rec)

    # ----------------------------------------------------
# Project Metrics
# ----------------------------------------------------

st.divider()

st.subheader("📋 Project Metrics")

metric_data = results.get("metrics", [])

if metric_data:

    try:

        metrics(metric_data)

    except Exception:

        metric = metric_data[0]

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Files",
            metric.get("total_files", 0),
        )

        c2.metric(
            "Lines",
            metric.get("total_lines", 0),
        )

        c3.metric(
            "Functions",
            metric.get("total_functions", 0),
        )

        c1, c2 = st.columns(2)

        c1.metric(
            "Classes",
            metric.get("total_classes", 0),
        )

        c2.metric(
            "Average Complexity",
            metric.get(
                "average_complexity",
                0,
            ),
        )

else:

    st.info("No project metrics available.")

# ----------------------------------------------------
# Complexity Table
# ----------------------------------------------------

st.divider()

st.subheader("⚙ Function Complexity")

complexity_data = results.get(
    "complexity",
    [],
)

if complexity_data:

    try:

        complexity(
            complexity_data
        )

    except Exception:

        st.dataframe(
            complexity_data,
            use_container_width=True,
            hide_index=True,
        )

else:

    st.success(
        "No complex functions detected."
    )

# ----------------------------------------------------
# Code Findings
# ----------------------------------------------------

st.divider()

st.subheader("🔍 Code Quality Findings")

finding_data = results.get(
    "findings",
    [],
)

if finding_data:

    try:

        findings(
            finding_data
        )

    except Exception:

        st.dataframe(
            finding_data,
            use_container_width=True,
            hide_index=True,
        )

else:

    st.success(
        "No code quality issues found."
    )

# ----------------------------------------------------
# Security Findings
# ----------------------------------------------------

st.divider()

st.subheader("🛡 Security Findings")

security_data = results.get(
    "security",
    [],
)

if security_data:

    try:

        security(
            security_data
        )

    except Exception:

        st.dataframe(
            security_data,
            use_container_width=True,
            hide_index=True,
        )

else:

    st.success(
        "🎉 No security vulnerabilities detected."
    )

# ----------------------------------------------------
# Overall Statistics
# ----------------------------------------------------

st.divider()

st.subheader("📈 Overall Statistics")

left, right = st.columns(2)

with left:

    st.metric(
        "Critical Issues",
        summary["critical"],
    )

    st.metric(
        "High Issues",
        summary["high"],
    )

with right:

    st.metric(
        "Medium Issues",
        summary["medium"],
    )

    st.metric(
        "Low Issues",
        summary["low"],
    )

    # ----------------------------------------------------
# Export Report
# ----------------------------------------------------

st.divider()

st.subheader("📄 Export Analysis")

import json
from datetime import datetime

report = {
    "project": project_name,
    "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "summary": summary,
    "metrics": results.get("metrics", []),
    "complexity": results.get("complexity", []),
    "findings": results.get("findings", []),
    "security": results.get("security", []),
    "ai_summary": results.get("ai_summary", ""),
}

json_report = json.dumps(
    report,
    indent=4,
)

st.download_button(
    label="📥 Download JSON Report",
    data=json_report,
    file_name=f"{project_name}_analysis.json",
    mime="application/json",
)

# ----------------------------------------------------
# Download Text Report
# ----------------------------------------------------

text_report = f"""
===================================================
               CODEGUARD AI REPORT
===================================================

Project
-------
{project_name}

Generated
---------
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Health Score
------------
{summary['health_score']}/100

Maintainability
---------------
{summary['maintainability']}/100

Security Issues
---------------
Critical : {summary['critical']}
High     : {summary['high']}
Medium   : {summary['medium']}
Low      : {summary['low']}

Code Findings
-------------
{summary['quality']}

AI Summary
----------
{results['ai_summary']}

===================================================
Generated using CodeGuard AI
===================================================
"""

st.download_button(
    label="📄 Download Text Report",
    data=text_report,
    file_name=f"{project_name}_report.txt",
    mime="text/plain",
)

# ----------------------------------------------------
# Quick Statistics
# ----------------------------------------------------

st.divider()

st.subheader("📌 Quick Statistics")

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        f"""
### 📁 Files

{results['metrics'][0]['total_files']}
"""
    )

with col2:

    st.info(
        f"""
### 🧩 Functions

{results['metrics'][0]['total_functions']}
"""
    )

with col3:

    st.info(
        f"""
### 🏛 Classes

{results['metrics'][0]['total_classes']}
"""
    )

# ----------------------------------------------------
# Navigation
# ----------------------------------------------------

st.divider()

left, middle, right = st.columns(3)

with left:

    if st.button(
        "📂 Analyze Another Project",
        use_container_width=True,
    ):

        st.session_state.project_path = None
        st.session_state.file_name = None

        st.switch_page("pages/Upload.py")

with middle:

    if st.button(
        "💬 AI Chat",
        use_container_width=True,
    ):

        st.switch_page("pages/Chat.py")

with right:

    if st.button(
        "🏠 Home",
        use_container_width=True,
    ):

        st.switch_page("Home.py")

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.divider()

st.markdown(
    """
<div style="text-align:center; padding:15px">

### 🛡 CodeGuard AI

AI Powered Secure Code Review Platform

Built using

🐍 Python • Ollama • Streamlit • AST Analysis

---

**Static Analysis | Security Review | AI Insights**

</div>
""",
    unsafe_allow_html=True,
)