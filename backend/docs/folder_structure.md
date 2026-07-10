# AI Code Review & Security Analysis Agent
# Folder Structure Documentation

---

# 1. Introduction

The AI Code Review & Security Analysis Agent follows a modular and scalable project structure to separate responsibilities such as API development, business logic, AI agents, security scanning, vector database operations, report generation, and frontend development.

This organization improves maintainability, scalability, testing, and collaboration.

---

# 2. Overall Project Structure

```

CodeGuard-AI-v2/

│

├── backend/

├── frontend/

├── docs/

├── knowledge_base/

├── vector_db/

├── workspace/

├── reports/

├── docker/

├── tests/

├── .env

├── docker-compose.yml

├── README.md

└── requirements.txt

```

---

# 3. Backend Structure

```

backend/

│

├── app/

│

├── api/

├── core/

├── database/

├── models/

├── repositories/

├── schemas/

├── services/

├── agents/

├── graph/

├── prompts/

├── vectorstore/

├── utils/

└── main.py

```

---

# 4. Folder Responsibilities

---

## api/

Contains all REST API endpoints.

Example

```

upload.py

analysis.py

security.py

reports.py

chat.py

```

Responsibilities

- Request validation
- Response formatting
- API routing

---

## core/

Contains project configuration.

Examples

```

config.py

logging.py

security.py

constants.py

```

Responsibilities

- Environment configuration
- Logging
- Authentication settings
- Global constants

---

## database/

Database configuration.

Files

```

session.py

base.py

migrations/

```

Responsibilities

- SQLAlchemy session
- Database engine
- Alembic migrations

---

## models/

Database models.

Examples

```

user.py

project.py

code_file.py

scan_job.py

scan_result.py

ai_review.py

```

Responsibilities

- ORM models
- Table definitions
- Relationships

---

## repositories/

Database access layer.

Examples

```

project_repository.py

scan_repository.py

review_repository.py

```

Responsibilities

- CRUD operations
- Query optimization
- Database abstraction

---

## schemas/

Pydantic models.

Examples

```

project.py

review.py

chat.py

```

Responsibilities

- Input validation
- API serialization
- Response models

---

## services/

Business logic layer.

Structure

```

services/

upload/

scanner/

analysis/

security/

remediation/

report/

rag/

vectorstore/

```

Responsibilities

- Upload handling
- Static analysis
- Security scanning
- AI orchestration support

---

## agents/

AI agents.

Structure

```

agents/

coordinator/

quality/

security/

remediation/

summary/

assistant/

```

Responsibilities

- Code Analysis Agent
- Security Agent
- Remediation Agent
- PR Summary Agent
- Conversational Assistant

---

## graph/

LangGraph workflow.

Files

```

graph.py

nodes.py

router.py

state.py

```

Responsibilities

- Multi-agent orchestration
- Workflow execution
- State management

---

## prompts/

Prompt templates.

Examples

```

security_prompt.txt

review_prompt.txt

summary_prompt.txt

chat_prompt.txt

```

Responsibilities

- LLM prompts
- Agent instructions
- System prompts

---

## vectorstore/

Vector database integration.

Files

```

embeddings.py

retriever.py

ingestion.py

```

Responsibilities

- Embedding generation
- ChromaDB indexing
- Similarity search

---

## utils/

Utility functions.

Examples

```

file_utils.py

validators.py

helpers.py

```

Responsibilities

- File handling
- Validation
- Common helper methods

---

# 5. Frontend Structure

```

frontend/

│

app.py

pages/

components/

assets/

styles/

```

Pages

```

Home

Upload

Dashboard

Analysis

Security

AI Review

Chat

Reports

Settings

```

---

# 6. Knowledge Base

```

knowledge_base/

│

OWASP/

CERT/

CWE/

Python/

Java/

```

Contents

- PDF files
- Markdown notes
- Secure coding guides
- Best practice documents

---

# 7. Vector Database

```

vector_db/

```

Stores

- Embeddings
- Metadata
- ChromaDB collections

Metadata Example

```

Source

Language

Topic

OWASP Category

Title

Section

```

---

# 8. Workspace

```

workspace/

```

Each uploaded project receives its own workspace.

Example

```

workspace/

9c1c1b3a/

source/

analysis/

reports/

```

---

# 9. Reports

```

reports/

```

Generated reports

- PDF
- HTML
- Markdown
- JSON

---

# 10. Tests

```

tests/

```

Structure

```

unit/

integration/

api/

```

Purpose

- Unit testing
- Integration testing
- API testing

---

# 11. Docker

```

docker/

```

Contains

- Dockerfiles
- Compose configuration
- Deployment scripts

---

# 12. Naming Conventions

Python files

```

snake_case.py

```

Classes

```

PascalCase

```

Functions

```

snake_case()

```

Constants

```

UPPER_CASE

```

Variables

```

snake_case

```

---

# 13. Coding Standards

- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions focused
- Apply SOLID principles
- Separate concerns
- Avoid duplicated code

---

# 14. Future Expansion

The structure supports adding:

- JavaScript analyzer
- Go analyzer
- C++ analyzer
- GitHub Pull Request integration
- VS Code extension
- CI/CD plugins
- Team dashboards
- AI test generation

without major restructuring.

---

# 15. Conclusion

The folder structure separates presentation, business logic, persistence, AI orchestration, and knowledge retrieval into independent modules. This modular organization supports maintainability, scalability, testing, and future enhancements while aligning with enterprise software architecture principles.

---

# References

1. FastAPI Project Structure Guidelines
2. SQLAlchemy Best Practices
3. LangGraph Documentation
4. ChromaDB Documentation
5. Clean Architecture by Robert C. Martin