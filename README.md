# 🛡️ CodeGuard v3

## AI Code Review & Security Analysis Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-green)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# Project Overview

CodeGuard v3 is an AI-powered Code Review & Security Analysis Platform designed to automate software code reviews using a multi-agent architecture.

The platform combines static code analysis, Retrieval-Augmented Generation (RAG), Large Language Models (Groq), and secure coding knowledge bases to identify code quality issues, detect OWASP-standard security vulnerabilities, generate remediation suggestions, and produce professional pull request summaries.

Developers can upload or paste Python and Java source code, receive AI-powered analysis, ask follow-up security questions, and export structured reports through a modern Streamlit dashboard.

---

# Problem Statement

Software development teams frequently struggle with:

- Inconsistent code quality
- Undetected security vulnerabilities
- Manual and time-consuming code reviews
- Lack of secure coding guidance
- Late detection of vulnerabilities
- Difficulty following OWASP secure coding standards

CodeGuard v3 addresses these challenges through an intelligent multi-agent AI platform that automates secure code review while providing explainable recommendations and developer-friendly remediation guidance.

---

# Key Features

✅ Python Code Analysis

✅ Java Code Analysis

✅ OWASP Security Detection

✅ AI Code Review

✅ AI Security Review

✅ AI Remediation

✅ Pull Request Summary Generation

✅ Severity Scoring

✅ Health Score Calculation

✅ RAG-powered Secure Coding Assistant

✅ ChromaDB Knowledge Base

✅ PostgreSQL Storage

✅ Streamlit Dashboard

✅ JSON Report Export

✅ Markdown Report Export

---

# Technology Stack

## Frontend

- Streamlit

## Backend

- Python 3.13

## AI

- Groq API
- Prompt Engineering

## Knowledge Retrieval

- LangChain
- ChromaDB
- Sentence Transformers

## Database

- PostgreSQL

## Knowledge Base

- OWASP Cheat Sheets
- CERT Secure Coding
- CWE
- Python Secure Coding
- Java Secure Coding

## Libraries

- SQLAlchemy
- PyPDFLoader
- RecursiveCharacterTextSplitter
- ReportLab
- python-dotenv
- Uvicorn

---

# 🏗️ System Architecture

```text
                    +---------------------------+
                    |     Streamlit Dashboard   |
                    +------------+--------------+
                                 |
                                 v
                  +-----------------------------+
                  |      Multi-Agent Engine      |
                  +-------------+---------------+
                                |
      ---------------------------------------------------------
      |               |               |              |         |
      v               v               v              v         v
+-------------+ +-------------+ +-------------+ +-------------+ +-------------+
| Code Agent  | | Security    | | Remediation | | Summary     | | Assistant   |
|             | | Agent       | | Agent       | | Agent       | | Agent       |
+------+------+ +------+------+ +------+------+ +------+------+ +------+------+
       |                |               |               |               |
       ---------------------------------------------------------------
                                |
                                v
                      +----------------------+
                      |     Groq LLM API     |
                      +----------+-----------+
                                 |
                                 v
                   +----------------------------+
                   |    RAG Knowledge Base      |
                   |     (ChromaDB + PDFs)      |
                   +------------+---------------+
                                |
        ---------------------------------------------------------
        |             |             |             |             |
        v             v             v             v             v
      OWASP         CERT          CWE         Python         Java
```

---

# 🤖 AI Agents

CodeGuard v3 follows a **Multi-Agent Architecture**, where each agent performs an independent task and contributes to the final analysis.

---

## 📋 1. Code Analysis Agent

### Responsibilities

- Detect code smells
- Missing documentation
- Poor naming conventions
- Complexity analysis
- Maintainability issues
- Best practice violations
- Error handling issues
- Readability improvements

### Output

- Static findings
- AI code review
- Severity statistics
- Execution time

---

## 🔒 2. Security Agent

### Responsibilities

Detect common software vulnerabilities including:

- SQL Injection
- Command Injection
- Unsafe eval()
- Hardcoded Secrets
- Path Traversal
- Weak Input Validation
- OWASP Top 10 vulnerabilities

### Output

- Security findings
- Severity classification
- AI security review
- Execution time

---

## 🛠️ 3. Remediation Agent

### Responsibilities

Uses Groq AI to:

- Explain detected issues
- Describe security risks
- Rewrite vulnerable code
- Apply secure coding practices
- Improve readability
- Improve maintainability
- Generate production-ready fixes

### Output

- Complete remediated code
- Secure implementation
- OWASP recommendations

---

## 📄 4. PR Summary Agent

### Responsibilities

Generate a professional Pull Request review including:

- Executive Summary
- Code Quality Summary
- Security Summary
- Severity Breakdown
- Health Score
- Risk Assessment
- Priority Fixes
- Overall Recommendation

### Output

Markdown Pull Request Report

---

## 💬 5. AI Assistant Agent

The Assistant combines **Retrieval-Augmented Generation (RAG)** with Groq AI.

### Features

- Answers secure coding questions
- Uses OWASP knowledge
- Uses CERT Secure Coding
- Uses CWE references
- Python secure coding guidance
- Java secure coding guidance
- AI-powered explanations
- Developer-friendly responses

---

# 📦 Core Modules

The platform consists of the following modules:

### Upload Module

- Upload Python files
- Upload Java files
- Paste source code
- Language selection

---

### Analysis Module

- Static Code Analysis
- Security Analysis
- AI Code Review
- AI Security Review

---

### Remediation Module

- AI Code Fix Generation
- Secure Code Recommendations
- Best Practice Suggestions

---

### Reporting Module

- Health Score
- Severity Metrics
- Pull Request Summary
- JSON Export
- Markdown Export

---

### Knowledge Module

- Document Loader
- Text Chunking
- Embedding Generation
- ChromaDB Indexing
- Semantic Search

---

### Assistant Module

- RAG Retrieval
- Context Building
- Groq Response Generation
- Secure Coding Guidance

---

# 🔄 Complete Workflow

```text
Developer
      │
      ▼
Upload Python / Java Code
      │
      ▼
Language Detection
      │
      ▼
Multi-Agent Orchestrator
      │
      ├──────────────────────► Code Analysis Agent
      │
      ├──────────────────────► Security Agent
      │
      ├──────────────────────► Remediation Agent
      │
      ├──────────────────────► Summary Agent
      │
      └──────────────────────► Assistant Agent
                                │
                                ▼
                           ChromaDB
                                │
                                ▼
                             Groq LLM
                                │
                                ▼
                        Final AI Responses
                                │
                                ▼
                     Streamlit Dashboard
                                │
                                ▼
                    Download Reports
```

---

# 🧠 Retrieval-Augmented Generation (RAG)

CodeGuard v3 uses a Retrieval-Augmented Generation pipeline for secure coding assistance.

```text
User Question
        │
        ▼
Retriever
        │
        ▼
Top Relevant Documents
        │
        ▼
Prompt Construction
        │
        ▼
Groq LLM
        │
        ▼
Professional Answer
```

### Knowledge Sources

- OWASP Cheat Sheets
- CERT Secure Coding Standards
- CWE Documentation
- Python Secure Coding Guide
- Java Secure Coding Guide

---

# 📊 Dashboard Overview

The Streamlit dashboard provides:

- 📤 Source Code Upload
- 📋 Code Analysis Results
- 🔒 Security Findings
- 🛠️ AI Remediation
- 📄 Pull Request Summary
- 💬 AI Assistant
- 📥 JSON Export
- 📥 Markdown Export
- 📈 Health Score
- 📊 Severity Dashboard


---

# 📁 Project Structure

```text
CodeGuard-AI-v3/
│
├── app/
│   ├── agents/
│   │   ├── assistant_agent.py
│   │   ├── code_agent.py
│   │   ├── remediation_agent.py
│   │   ├── security_agent.py
│   │   └── summary_agent.py
│   │
│   ├── analyzers/
│   │   ├── python_analyzer.py
│   │   └── java_analyzer.py
│   │
│   ├── api/
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   ├── models.py
│   │   └── session.py
│   │
│   ├── rag/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   └── indexer.py
│   │
│   ├── services/
│   │   ├── groq_service.py
│   │   └── orchestrator.py
│   │
│   ├── static/
│   ├── templates/
│   └── utils/
│
├── assets/
│   ├── logo.png
│   └── style.css
│
├── knowledge_base/
│   └── pdfs/
│       ├── CERT/
│       ├── CWE/
│       ├── Java/
│       ├── OWASP/
│       └── Python/
│
├── vector_db/
│
├── uploads/
│
├── reports/
│
├── streamlit_pages/
│   ├── dashboard.py
│   ├── assistant.py
│   ├── reports.py
│   └── about.py
│
├── streamlit_app.py
├── build_kb.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/BharkaviPM/CodeGuard-ai.git

cd CodeGuard-ai
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file in the project root.

```env
# ===========================
# Groq
# ===========================

GROQ_API_KEY=your_groq_api_key

# ===========================
# Application
# ===========================

APP_NAME=CodeGuard v3

APP_VERSION=1.0.0

DEBUG=True

# ===========================
# PostgreSQL
# ===========================

DB_HOST=localhost

DB_PORT=5432

DB_NAME=codeguard_v3

DB_USER=postgres

DB_PASSWORD=your_password

# ===========================
# Knowledge Base
# ===========================

KNOWLEDGE_BASE=knowledge_base/pdfs

CHROMA_DB=vector_db

UPLOAD_FOLDER=uploads

REPORT_FOLDER=reports
```

---

# 🐘 PostgreSQL Setup

Create the database.

```sql
CREATE DATABASE codeguard_v3;
```

Verify the database connection.

```bash
python -m tests.test_connection
```

Expected Output

```text
Connected Successfully!
PostgreSQL 17.x
```

---

# 🧠 Build Knowledge Base

Index all secure coding documents.

```bash
python -m build_kb
```

Expected Output

```text
Loading documents...

Loaded 258 pages

Created 737 chunks

Knowledge Base Indexed Successfully
```

---

# ▶️ Running the Project

## Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

## Start Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

Open

```
http://localhost:8501
```

---

# 🧪 Running Unit Tests

Configuration

```bash
python -m tests.test_config
```

Database

```bash
python -m tests.test_connection
```

Knowledge Base

```bash
python -m tests.test_rag
```

Code Analysis Agent

```bash
python -m tests.test_code_agent
```

Security Agent

```bash
python -m tests.test_security_agent
```

Remediation Agent

```bash
python -m tests.test_remediation_agent
```

Summary Agent

```bash
python -m tests.test_summary_agent
```

Assistant Agent

```bash
python -m tests.test_assistant_agent
```

---

# 📸 Screenshots

Add screenshots of the application in this section.

Suggested screenshots:

- Dashboard
- Upload Source Code
- Code Analysis Results
- Security Findings
- AI Remediation
- Pull Request Summary
- AI Assistant
- Reports Page
- About Page

Example

```text
screenshots/

dashboard.png

security.png

remediation.png

assistant.png

reports.png
```

---

---

# 🎯 Milestone 3 Deliverables

The following deliverables have been successfully completed in **CodeGuard v3**.

## ✅ AI Code Analysis

- Python Static Analysis
- Java Static Analysis
- Code Smell Detection
- Best Practice Recommendations
- AI Code Review

---

## ✅ Security Analysis

Implemented security detection for:

- SQL Injection
- Command Injection
- Unsafe eval()
- Hardcoded Secrets
- Path Traversal

AI-powered security review is generated using the Groq LLM with OWASP secure coding guidance.

---

## ✅ AI Remediation

Automatically generates:

- Explanation of vulnerabilities
- Secure implementation
- Complete rewritten code
- OWASP-compliant recommendations
- Maintainability improvements

---

## ✅ Pull Request Summary

Generates a professional Pull Request review including:

- Executive Summary
- Code Quality Review
- Security Review
- Health Score
- Severity Breakdown
- Risk Assessment
- Priority Fixes
- Overall Recommendation

---

## ✅ Secure Coding Assistant

Features:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Secure Coding Guidance
- OWASP Knowledge
- CERT Secure Coding
- CWE References
- Python Secure Coding
- Java Secure Coding

---

## ✅ Dashboard

Provides:

- Source Code Upload
- Source Code Viewer
- Project Overview
- Health Score
- Severity Dashboard
- Code Findings
- Security Findings
- AI Reviews
- AI Remediation
- Pull Request Summary
- Export Reports

---

# 📈 Project Achievements

✔ Multi-Agent AI Architecture

✔ Retrieval-Augmented Generation (RAG)

✔ ChromaDB Knowledge Base

✔ PostgreSQL Integration

✔ Groq LLM Integration

✔ Streamlit Dashboard

✔ AI-powered Code Review

✔ AI-powered Security Analysis

✔ AI-generated Secure Code

✔ AI Pull Request Summary

✔ JSON Report Export

✔ Markdown Report Export

---

# 🚀 Future Enhancements (Milestone 4)

The following enhancements are planned for the next version.

### Security

- XSS Detection
- CSRF Detection
- SSRF Detection
- Weak Cryptography Detection
- Insecure File Upload Detection
- Broken Authentication Detection
- Broken Access Control Detection
- Insecure Deserialization Detection

---

### Code Quality

- Cyclomatic Complexity
- Duplicate Code Detection
- Dead Code Detection
- Long Method Detection
- Magic Number Detection
- Dependency Analysis

---

### Artificial Intelligence

- Repository-Level Review
- Multi-file Analysis
- Cross-file Vulnerability Detection
- AI Risk Prediction
- AI Fix Confidence Score
- Code Quality Trend Analysis

---

### Reporting

- PDF Report Export
- Excel Report Export
- Historical Report Storage
- Project Comparison Dashboard

---

### Dashboard

- Interactive Charts
- Trend Analytics
- Vulnerability Timeline
- Repository Statistics

---

### DevOps

- Docker Support
- GitHub Actions
- CI/CD Integration
- Git Pre-Commit Hooks

---

# 📌 Current Version

| Component | Status |
|-----------|--------|
| Code Analysis Agent | ✅ Completed |
| Security Agent | ✅ Completed |
| Remediation Agent | ✅ Completed |
| PR Summary Agent | ✅ Completed |
| AI Assistant | ✅ Completed |
| Dashboard | ✅ Completed |
| PostgreSQL | ✅ Completed |
| ChromaDB | ✅ Completed |
| RAG Pipeline | ✅ Completed |
| Knowledge Base | ✅ Completed |

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature/my-feature
```

5. Create a Pull Request

---

# 📄 License

This project is released under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the MIT License.

---

# 👨‍💻 Author

**Bharkavi P M**

AI Engineer | Python Developer | Full Stack Developer

GitHub:

https://github.com/BharkaviPM

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the following technologies:

- Python
- Streamlit
- PostgreSQL
- ChromaDB
- Groq
- LangChain
- Sentence Transformers
- OWASP Foundation
- CERT Secure Coding
- CWE
- Hugging Face

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork the repository

🛠️ Contribute improvements

📢 Share your feedback

---

# 🛡️ CodeGuard v3

**AI Code Review & Security Analysis Platform**

Built with ❤️ using Python, Streamlit, PostgreSQL, ChromaDB, and Groq.

---

## 📚 Repository Status

**Version:** 1.0.0

**Release:** CodeGuard v3

**Architecture:** Multi-Agent AI + RAG

**Development Status:** Milestone 3 Completed ✅