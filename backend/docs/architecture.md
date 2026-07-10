# AI Code Review & Security Analysis Agent
# System Architecture

---

# 1. Introduction

The AI Code Review & Security Analysis Agent is a multi-agent software platform that automatically analyzes source code for quality issues, security vulnerabilities, and secure coding violations. The system combines static analysis tools, Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and LangGraph-based multi-agent orchestration to provide developers with intelligent, explainable, and actionable code reviews.

The architecture follows a modular, service-oriented design to ensure scalability, maintainability, and extensibility.

---

# 2. Objectives

The architecture is designed to:

- Support Python and Java code analysis.
- Detect security vulnerabilities using industry-standard tools.
- Generate AI-powered remediation suggestions.
- Provide conversational code assistance using RAG.
- Produce structured review reports.
- Support future language extensions.

---

# 3. High-Level Architecture

```

                        Developer

                            │

                            ▼

                  Streamlit Frontend

                            │

                            ▼

                     FastAPI Backend

                            │

        ┌───────────────────┼────────────────────┐

        ▼                   ▼                    ▼

Authentication       Project Service       Report Service

                            │

                            ▼

                    Code Submission Module

                 (Paste / Upload Python & Java)

                            │

                            ▼

                     Workspace Manager

                            │

                            ▼

                      Project Scanner

                            │

                            ▼

                 Static Analysis Pipeline

       ┌───────────┬───────────┬───────────┬────────────┐

       ▼           ▼           ▼           ▼

     AST        Flake8      Pylint      Radon

       ▼           ▼           ▼           ▼

      Bandit   Semgrep   detect-secrets  pip-audit

                            │

                            ▼

                 LangGraph Coordinator

                            │

      ┌───────────┬───────────┬───────────┬──────────┐

      ▼           ▼           ▼           ▼

Code Analysis  Security  Remediation  PR Summary

      │                                   │

      └───────────────┬───────────────────┘

                      ▼

            Conversational Assistant

                      │

                      ▼

                    RAG Layer

                      │

              ChromaDB Vector Store

                      │

          OWASP • CERT • CWE • Python

               Java Secure Coding

                      │

                      ▼

                   Ollama LLM

                      │

                      ▼

             AI Generated Response

                      │

                      ▼

              Report Generator

                      │

        PDF • HTML • Markdown • JSON

                      │

                      ▼

                PostgreSQL Database

```

---

# 4. Component Description

## 4.1 Streamlit Frontend

Responsibilities

- User Login
- Project Dashboard
- Upload Code
- Paste Code
- View Findings
- Chat Interface
- Reports
- Settings

---

## 4.2 FastAPI Backend

Responsibilities

- REST APIs
- Authentication
- Request Validation
- Project Management
- AI Agent Execution
- Report Generation

---

## 4.3 Code Submission Module

Supports

- Python Files (.py)
- Java Files (.java)
- Paste Code
- Syntax Validation
- File Validation
- UTF-8 Validation

---

## 4.4 Workspace Manager

Responsibilities

- Create Project Folder
- Store Uploaded Files
- Temporary Files
- Reports
- Cache

---

## 4.5 Scanner Manager

Responsibilities

- Scan Uploaded Project
- Detect Language
- Ignore Build Folders
- Create File Metadata
- Trigger Analysis Pipeline

---

# 5. Static Analysis Pipeline

The scanner invokes multiple analysis tools.

## AST Analyzer

Detects

- Functions
- Classes
- Imports
- Complexity Indicators

---

## Flake8

Detects

- Style Violations
- PEP8 Errors
- Unused Imports

---

## Pylint

Detects

- Code Smells
- Naming Problems
- Missing Documentation
- Refactoring Suggestions

---

## Radon

Calculates

- Cyclomatic Complexity
- Maintainability Index
- Halstead Metrics

---

## Bandit

Detects

- SQL Injection
- Command Injection
- Weak Hashing
- Insecure Deserialization

---

## Semgrep

Detects

- OWASP Vulnerabilities
- Security Rules
- Custom Rules

---

## detect-secrets

Detects

- API Keys
- Tokens
- Passwords

---

## pip-audit

Detects

- Dependency Vulnerabilities
- CVEs

---

# 6. Multi-Agent Architecture

The system uses LangGraph to coordinate multiple specialized AI agents.

```

Coordinator Agent

│

├── Code Analysis Agent

├── Security Vulnerability Agent

├── Remediation Agent

├── PR Summary Agent

└── Conversational Assistant

```

---

# 7. Agent Responsibilities

## Coordinator Agent

Responsibilities

- Workflow orchestration
- Agent scheduling
- Context management

---

## Code Analysis Agent

Responsibilities

- Code Smells
- SOLID Violations
- Maintainability
- Complexity
- Naming
- Architecture Review

---

## Security Vulnerability Agent

Responsibilities

- OWASP Detection
- Vulnerability Severity
- Security Recommendations
- Dependency Analysis

---

## Remediation Agent

Responsibilities

- Explain Vulnerabilities
- Generate Fixed Code
- Explain Best Practices
- Secure Refactoring

---

## PR Summary Agent

Responsibilities

- Executive Summary
- Quality Score
- Security Score
- Overall Recommendations

---

## Conversational Assistant

Responsibilities

- Question Answering
- Explain Findings
- Secure Coding Guidance
- Code Examples

---

# 8. LangGraph Workflow

```

Upload Code

↓

Scanner

↓

Coordinator Agent

↓

Code Analysis Agent

↓

Security Agent

↓

Remediation Agent

↓

Summary Agent

↓

RAG Assistant

↓

Final Report

```

---

# 9. RAG Architecture

```

Knowledge Documents

↓

PyMuPDF

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

ChromaDB

↓

Retriever

↓

Prompt

↓

Ollama

↓

Generated Answer

```

---

# 10. Database Architecture

Main Tables

- users
- projects
- code_files
- scan_jobs
- scan_results
- ai_reviews
- knowledge_chunks
- embeddings

---

# 11. Security Architecture

Security Features

- JWT Authentication
- Password Hashing
- HTTPS
- Environment Variables
- Input Validation
- Rate Limiting
- Secure File Upload
- RBAC

---

# 12. Deployment Architecture

```

Developer

↓

Browser

↓

Streamlit

↓

FastAPI

↓

PostgreSQL

↓

ChromaDB

↓

Ollama

```

---

# 13. Technology Stack

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Vector Store | ChromaDB |
| LLM | Ollama |
| Multi-Agent | LangGraph |
| AI Framework | LangChain |
| Security | Bandit, Semgrep |
| Static Analysis | Flake8, Pylint, Radon |
| Reports | ReportLab |

---

# 14. Future Enhancements

- Multi-language Support
- VS Code Extension
- GitHub Pull Request Review
- CI/CD Integration
- Team Collaboration
- Historical Trend Analysis
- AI Unit Test Generation

---

# 15. Conclusion

The proposed architecture provides a scalable, modular, and AI-driven platform for automated code review and security analysis. By combining static analysis, security scanning, LangGraph-based orchestration, Retrieval-Augmented Generation, and local LLM inference, the platform delivers explainable, actionable, and context-aware recommendations while remaining extensible for future enhancements.

---

# References

1. OWASP Top 10 (2021)
2. LangGraph Documentation
3. LangChain Documentation
4. ChromaDB Documentation
5. FastAPI Documentation
6. Streamlit Documentation
7. SQLAlchemy Documentation
8. Ollama Documentation