# CodeGuard AI



## AI Code Review & Security Analysis Agent



**Milestone 1 Completion Report**



---



# Project Overview



CodeGuard AI is an AI-powered Code Review and Security Analysis platform designed to automate secure code reviews, detect security vulnerabilities, identify code quality issues, and provide intelligent remediation suggestions using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and a future multi-agent architecture.



The project aims to reduce manual review effort while improving code quality and secure coding practices throughout the software development lifecycle.



---



# Project Statement



Software development teams frequently struggle with:



* Inconsistent code quality

* Undetected security vulnerabilities

* Time-consuming manual code reviews

* Lack of immediate secure coding guidance

* Difficulty enforcing OWASP and secure coding standards



CodeGuard AI addresses these challenges by combining static analysis, AI reasoning, and knowledge retrieval into an intelligent review platform.



---



# Technology Stack



## Backend



* FastAPI

* Python 3.13



## AI Stack



* Ollama

* Llama 3

* LangChain

* ChromaDB

* Nomic Embed Text



## Database



* PostgreSQL



## Vector Database



* ChromaDB



## Document Processing



* PyPDF

* LangChain Document Loaders

* Recursive Character Text Splitter



## Development Tools



* Uvicorn

* Pydantic

* SQLAlchemy

* Alembic



---



# Milestone 1 Objectives



The first milestone focused on building the foundational infrastructure required for AI-assisted secure code review.



---



# Completed Features



## 1. Project Architecture



Designed the complete backend architecture including:



* Modular project structure

* Service layer

* API layer

* Database layer

* RAG layer

* Knowledge Base

* Upload Workspace



---



## 2. Database Layer



Implemented PostgreSQL integration with SQLAlchemy.



Completed:



* Database connection

* Configuration management

* Session management

* Base models

* Upload metadata storage



---



## 3. Code Submission Module



Implemented secure code submission support.



Features include:



* Python file upload

* Java file upload

* Direct code submission

* Workspace storage

* Syntax validation

* Metadata persistence



---



## 4. Secure Coding Knowledge Base



Constructed the initial knowledge repository using authoritative secure coding documentation.



Knowledge sources include:



* OWASP Cheat Sheets

* Secure Coding Standards

* Java Secure Coding Guidelines

* SQL Injection Prevention

* Authentication Best Practices

* Cryptography Guidelines



---



## 5. Document Processing Pipeline



Implemented an ingestion pipeline capable of:



* Loading PDF documents

* Splitting documents into semantic chunks

* Preparing embeddings

* Indexing documents into ChromaDB



---



## 6. Embedding Pipeline



Integrated:



* nomic-embed-text



Capabilities:



* Vector generation

* Semantic similarity search

* Efficient retrieval



---



## 7. Chroma Vector Database



Implemented persistent vector storage.



Capabilities:



* Persistent vector index

* Semantic document retrieval

* Similarity search

* Context retrieval



---



## 8. Retrieval-Augmented Generation (RAG)



Built an end-to-end Retrieval-Augmented Generation pipeline.



Workflow:



User Question



↓



Retriever



↓



Relevant Knowledge



↓



Prompt Construction



↓



Llama 3



↓



AI Response



---



## 9. Conversational Code Assistant



Implemented an AI-powered assistant capable of answering secure coding questions.



Capabilities:



* Secure coding guidance

* OWASP explanations

* Best practices

* Vulnerability explanations

* Context-aware responses

* Source document references



Example:



Question:



> What is SQL Injection?



Response:



* AI-generated explanation

* Retrieved from OWASP documentation

* Source references returned



---



## 10. FastAPI REST API



Implemented REST endpoints for:



* Code upload

* File validation

* Conversational AI endpoint



Successfully tested using Swagger UI.



---



# Project Structure



```

backend/

│

├── app/

│   ├── api/

│   ├── core/

│   ├── database/

│   ├── models/

│   ├── schemas/

│   ├── services/

│   ├── rag/

│   ├── uploads/

│   └── main.py

│

├── chroma_db/

├── knowledge_base/

├── workspace/

├── requirements.txt

└── README.md

```



---



# Current System Workflow



```

User



↓



Upload Code



↓



Validation



↓



Storage



↓



User Question



↓



Retriever



↓



ChromaDB



↓



Relevant Documents



↓



Prompt Builder



↓



Ollama (Llama 3)



↓



AI Response

```



---



# Milestone 1 Deliverables



| Deliverable              | Status      |

| ------------------------ | ----------- |

| Project Architecture     | Completed |

| PostgreSQL Integration   | Completed |

| File Upload Module       | Completed |

| Syntax Validation        | Completed |

| Knowledge Base           | Completed |

| PDF Loader               | Completed |

| Chunking Pipeline        | Completed |

| Embeddings               | Completed |

| ChromaDB                 | Completed |

| Retriever                | Completed |

| RAG Pipeline             | Completed |

| Ollama Integration       | Completed |

| Conversational Assistant | Completed |

| FastAPI APIs             | Completed |

| Swagger Testing          | Completed |



---



# Current Limitations



The current implementation is intentionally modular and educational. While fully functional, it is not yet production-grade.



Current limitations include:



* RAG services are initialized per request.

* Ollama client is not cached.

* Retriever instances are recreated for each query.

* Prompt templates are tightly coupled with business logic.

* Limited structured logging.

* Basic exception handling.

* No dependency injection for AI services.

* No request tracing or metrics.

* No LangGraph orchestration.

* No agent coordination layer.

* Static analysis tools are not yet integrated.



These limitations will be addressed in Milestone 2.



---



# Milestone 2 Roadmap



Milestone 2 introduces the intelligent multi-agent analysis pipeline.



Planned components include:



## Static Analysis Agent



* AST Analysis

* Radon

* Flake8

* Pylint

* Complexity Analysis

* Code Smell Detection



## Security Agent



* Bandit

* Semgrep

* Detect Secrets

* pip-audit

* OWASP Mapping



## LangGraph Coordinator



Responsible for orchestrating all AI agents.



Workflow:



```

Coordinator



├── Static Analysis Agent



├── Security Agent



├── AI Review Agent



├── Remediation Agent



└── PR Summary Agent

```



## AI Review



* LLM-based code review

* Design recommendations

* Best practices

* Secure coding improvements



## Remediation Agent



* Suggested code fixes

* Secure alternatives

* Explanation of vulnerabilities



## Pull Request Summary Agent



Automatically generates:



* Executive Summary

* Issues Found

* Severity Breakdown

* Recommended Fixes



---



# Future Enhancements



* GitHub Pull Request Integration

* GitLab Integration

* CI/CD Pipeline Support

* VS Code Extension

* Docker Deployment

* Kubernetes Deployment

* Authentication & Authorization

* Redis Caching

* Background Workers

* Monitoring & Observability

* Multi-language Support

* Enterprise Dashboard



---



# Milestone 1 Status



**Status:** Completed



The foundational infrastructure for CodeGuard AI has been successfully implemented.



The system now supports:



* AI-powered secure coding assistance

* Retrieval-Augmented Generation (RAG)

* Persistent knowledge retrieval

* Conversational querying

* Secure document indexing

* RESTful API interaction



This milestone establishes a strong foundation for the production-grade multi-agent architecture that will be developed in Milestone 2.



---



# Next Milestone



**Milestone 2 – Static Analysis & Multi-Agent Architecture**



Focus areas:



* Production-grade RAG refactoring

* Static code analysis

* Security vulnerability detection

* LangGraph orchestration

* Multi-agent collaboration

* AI-assisted remediation

* Automated review summaries