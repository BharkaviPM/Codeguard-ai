# 🛡️ CodeGuard AI v3

## AI-Powered Multi-Agent Code Review & Security Analysis Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-green)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Project Overview

CodeGuard AI v3 is an AI-powered Multi-Agent Code Review and Security Analysis Platform that automates software code reviews, vulnerability detection, performance analysis, remediation generation, and secure coding guidance.

The platform combines:

- Multi-Agent AI Architecture
- Groq LLM
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- OWASP Knowledge Base
- Streamlit Dashboard
- Automated PDF Reporting

Developers can upload or paste Python and Java source code, receive AI-powered reviews, identify security vulnerabilities, generate secure code fixes, and download professional analysis reports.

---

# 🎯 Problem Statement

Software teams frequently face:

- Inconsistent code reviews
- Security vulnerabilities reaching production
- Time-consuming manual review processes
- Lack of secure coding knowledge
- Poor code maintainability
- Performance bottlenecks
- Difficulty following OWASP standards

CodeGuard AI solves these challenges using specialized AI agents that analyze source code from multiple perspectives and generate actionable recommendations.

---

# ✨ Features

## 🔍 Code Analysis

- Python Code Review
- Java Code Review
- Code Smell Detection
- Best Practice Validation
- Maintainability Analysis
- Readability Improvements

## 🔒 Security Analysis

- OWASP Vulnerability Detection
- SQL Injection Detection
- Command Injection Detection
- Unsafe eval() Detection
- Hardcoded Secret Detection
- Path Traversal Detection
- Security Severity Classification

## ⚡ Performance Analysis

- Time Complexity Review
- Space Complexity Review
- Nested Loop Detection
- Scalability Analysis
- Memory Usage Review
- Performance Optimization Suggestions

## 📊 Risk Assessment

- Risk Scoring
- Severity Classification
- Health Assessment
- Business Impact Evaluation
- Risk Prioritization

## 🛠️ AI Remediation

- Vulnerability Explanations
- Secure Code Suggestions
- Refactoring Recommendations
- OWASP-Compliant Fixes
- Production-Ready Improvements

## 💬 Secure Coding Assistant

- RAG-Powered Chatbot
- OWASP Guidance
- CWE References
- CERT Secure Coding Standards
- Context-Aware Security Answers

## 📄 Reporting

- PDF Report Export
- Executive Summary
- Security Findings
- Performance Findings
- Risk Assessment
- Remediation Recommendations

---

# 🏗️ System Architecture

```text
                Streamlit Dashboard
                         │
                         ▼
                  ReviewWorkflow
                         │
     ┌───────────────────┼───────────────────┐
     ▼                   ▼                   ▼

 Code Agent      Security Agent    Performance Agent
     │                   │                   │
     └───────────────────┼───────────────────┘
                         ▼

                    Risk Agent
                         │
                         ▼

               Remediation Agent
                         │
                         ▼

                  Summary Agent
                         │
                         ▼

                    PDF Report


                 Secure Coding Assistant
                           │
                           ▼

                    ChromaDB Vector DB
                           │
                           ▼

                     Knowledge Base
                           │
                           ▼

                        Groq LLM
```

---

# 🤖 AI Agents

## 📋 1. Code Analysis Agent

### Responsibilities

- Detect code smells
- Analyze maintainability
- Review coding standards
- Evaluate readability
- Identify best practice violations

### Output

- Code Quality Review
- Severity Assessment
- Improvement Suggestions

---

## 🔒 2. Security Agent

### Responsibilities

- Detect OWASP vulnerabilities
- Identify insecure coding practices
- Discover hardcoded credentials
- Analyze input validation

### Output

- Security Findings
- Severity Ratings
- Vulnerability Explanations

---

## ⚡ 3. Performance Agent

### Responsibilities

- Analyze algorithm efficiency
- Detect nested loops
- Identify scalability issues
- Suggest optimizations

### Output

- Performance Findings
- Optimization Suggestions
- Complexity Analysis

---

## 📊 4. Risk Assessment Agent

### Responsibilities

- Calculate overall risk
- Evaluate business impact
- Prioritize findings

### Output

- Risk Report
- Severity Breakdown
- Project Health Evaluation

---

## 🛠️ 5. Remediation Agent

### Responsibilities

- Generate secure code fixes
- Improve maintainability
- Recommend best practices

### Output

- Secure Code Suggestions
- Refactoring Recommendations
- OWASP Guidance

---

## 📄 6. Summary Agent

### Responsibilities

- Consolidate all findings
- Generate executive summaries
- Create final recommendations

### Output

- Final Review Report
- Executive Summary
- Action Plan

---

## 💬 7. Secure Coding Assistant

### Responsibilities

- Answer security questions
- Retrieve knowledge base context
- Provide secure coding guidance

### Output

- AI-Powered Responses
- OWASP References
- Security Recommendations

---

# 🧠 Retrieval-Augmented Generation (RAG)

CodeGuard AI includes a Retrieval-Augmented Generation pipeline for secure coding assistance.

```text
User Question
      │
      ▼

Document Retriever
      │
      ▼

Relevant Knowledge Chunks
      │
      ▼

Prompt Construction
      │
      ▼

Groq LLM
      │
      ▼

Security-Aware Response
```

### Knowledge Sources

- OWASP Cheat Sheets
- CWE Documentation
- CERT Secure Coding Standards
- Python Security Guidelines
- Java Security Guidelines

---

# 🛠️ Technology Stack

| Layer | Technology |
|---------|------------|
| Frontend | Streamlit |
| Programming Language | Python 3.13 |
| LLM | Groq |
| AI Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Data Processing | Pandas |
| Visualization | Plotly |
| Report Generation | ReportLab |
| Knowledge Base | OWASP, CERT, CWE |

---

# 📁 Project Structure

```text
CodeGuard-ai/

├── agents/
│   ├── code_analysis_agent.py
│   ├── security_agent.py
│   ├── performance_agent.py
│   ├── remediation_agent.py
│   ├── risk_agent.py
│   ├── summary_agent.py
│   └── chat_agent.py
│
├── workflows/
│   ├── review_workflow.py
│   ├── review_graph.py
│   └── state.py
│
├── services/
│   ├── groq_service.py
│   └── code_chat_service.py
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── chat_service.py
│
├── reports/
│   ├── pdf_generator.py
│   ├── markdown_report.py
│   └── chart_generator.py
│
├── utils/
│   ├── security_score.py
│   ├── health_score.py
│   ├── severity_parser.py
│   └── dashboard_metrics.py
│
├── tests/
├── vector_db/
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/BharkaviPM/Codeguard-ai.git

cd Codeguard-ai
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

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
GROQ_API_KEY=your_groq_api_key

GROQ_MODEL=llama-3.3-70b-versatile

CHROMA_DB_PATH=vector_db
```

---

# 🧠 Build Knowledge Base

```bash
python index_knowledge_base.py
```

Expected Output:

```text
Loading documents...
Creating embeddings...
Building vector database...
Knowledge Base Indexed Successfully
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 📊 Dashboard Features

The dashboard includes:

- 📤 Source Code Upload
- 📋 Code Review Results
- 🔒 Security Findings
- ⚡ Performance Analysis
- 📊 Risk Assessment
- 🛠️ Remediation Suggestions
- 📄 Executive Summary
- 💬 Secure Coding Assistant
- 📈 Severity Dashboard
- 📄 PDF Export

---

# 📸 Screenshots

## Dashboard

Add screenshot here:

```text
screenshots/dashboard.png
<img width="1874" height="891" alt="Image" src="https://github.com/user-attachments/assets/084dad45-eb95-4039-9c37-fa05530cb4f5" />
<img width="1812" height="856" alt="Image" src="https://github.com/user-attachments/assets/175b4ca6-5e20-4307-b11e-ed11eab94858" />
```

## Security Analysis

```text
screenshots/security.png
<img width="1812" height="856" alt="Image" src="https://github.com/user-attachments/assets/6b1ad62b-3419-41d6-8606-1aa414e3a0aa" />
<img width="1852" height="862" alt="Image" src="https://github.com/user-attachments/assets/2d78bb71-d738-4fbb-8863-7dd973495111" />

```

## Performance Review

```text
screenshots/performance.png
<img width="1817" height="840" alt="Image" src="https://github.com/user-attachments/assets/9608b312-6828-456e-9cf7-c8438581f464" />
```

## Risk Assessment

```text
screenshots/risk.png
<img width="1843" height="857" alt="Image" src="https://github.com/user-attachments/assets/9b5a7e96-fd71-4e61-82ae-162b1e47b6f2" />

```

## PDF Report

```text
screenshots/report.png
<img width="1863" height="910" alt="Image" src="https://github.com/user-attachments/assets/d47fec92-ff54-4cae-ab70-e9370bf806e1" />
```

---

# 🧪 Running Tests

```bash
python -m tests.test_groq
```

```bash
python -m tests.test_rag
```

```bash
python -m tests.test_security_agent
```

```bash
python -m tests.test_workflow
```

```bash
python -m tests.test_pdf
```

---

# 📈 Current Project Status

| Component | Status |
|------------|---------|
| Streamlit Dashboard | ✅ |
| Code Analysis Agent | ✅ |
| Security Agent | ✅ |
| Performance Agent | ✅ |
| Risk Assessment Agent | ✅ |
| Remediation Agent | ✅ |
| Summary Agent | ✅ |
| RAG Assistant | ✅ |
| ChromaDB Integration | ✅ |
| Groq Integration | ✅ |
| PDF Report Export | ✅ |
| Knowledge Base Indexing | ✅ |

---

# 🎯 Milestone Progress

## Phase 1 – Foundation ✅

- Project Structure
- RAG Pipeline
- ChromaDB Setup
- Groq Integration

## Phase 2 – Multi-Agent System ✅

- Code Analysis Agent
- Security Agent
- Remediation Agent
- Summary Agent

## Phase 3 – Advanced Review System ✅

- Performance Agent
- Risk Assessment Agent
- Dashboard Enhancements
- PDF Reporting

## Phase 4 – Planned

- LangGraph Parallel Execution
- Bandit Integration
- Pylint Integration
- Radon Complexity Analysis
- GitHub Repository Scanning
- ZIP Project Upload
- CI/CD Integration

---

# 📌 Version Information

| Item | Value |
|--------|--------|
| Version | 3.1.0 |
| Project | CodeGuard AI |
| Architecture | Multi-Agent + RAG |
| Status | Active Development |

---

# 🤝 Contributing

1. Fork the repository

2. Create a branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Add feature"
```

4. Push changes

```bash
git push origin feature/new-feature
```

5. Create Pull Request

---

# 👨‍💻 Author

**Bharkavi P M**

AI Engineer | Python Developer | Generative AI Enthusiast

GitHub:
https://github.com/BharkaviPM

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛠️ Contribute improvements
- 📢 Share feedback

---

# 📄 License

This project is licensed under the MIT License.

---

## 🛡️ CodeGuard AI v3

AI-Powered Multi-Agent Code Review & Security Analysis Platform

Built with ❤️ using Python, Streamlit, Groq, ChromaDB, LangChain, and ReportLab.
