# AI Code Review & Security Analysis Agent
# Database Design

---

# 1. Introduction

The AI Code Review & Security Analysis Agent requires two storage systems:

1. PostgreSQL
2. ChromaDB

PostgreSQL stores structured application data such as users, projects, scan results, AI reviews, and reports.

ChromaDB stores vector embeddings generated from secure coding documents for Retrieval-Augmented Generation (RAG).

---

# 2. Database Architecture

```

                 PostgreSQL

+------------------------------------+

| Users                              |

| Projects                           |

| Code Files                         |

| Scan Jobs                          |

| Scan Results                       |

| AI Reviews                         |

| Reports                            |

+------------------------------------+

                 ▲

                 │

                 ▼

               ChromaDB

+------------------------------------+

| Knowledge Chunks                   |

| Embeddings                         |

| Metadata                           |

+------------------------------------+

```

---

# 3. Entity Relationship Diagram (ERD)

```

Users

│

└───────────────┐

                │

Projects

│

├────────────── CodeFiles

│

├────────────── ScanJobs

│                    │

│                    ▼

│             ScanResults

│                    │

│                    ▼

│              AIReviews

│                    │

│                    ▼

└────────────── Reports

```

---

# 4. Database Tables

---

## 4.1 Users

Purpose

Stores registered users.

Fields

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary Key |
| username | VARCHAR | Unique username |
| email | VARCHAR | Email |
| password_hash | TEXT | Hashed password |
| role | VARCHAR | Admin/User |
| created_at | TIMESTAMP | Registration time |

Relationship

```

User

↓

Many Projects

```

---

## 4.2 Projects

Purpose

Stores uploaded projects.

Fields

| Column | Type |
|--------|------|
| id | UUID |
| user_id | UUID |
| project_name | VARCHAR |
| language | VARCHAR |
| upload_type | VARCHAR |
| created_at | TIMESTAMP |
| status | VARCHAR |

Relationship

```

Project

↓

Many Code Files

↓

Many Scan Jobs

```

---

## 4.3 Code Files

Purpose

Stores uploaded source files.

Fields

| Column | Type |
|--------|------|
| id | UUID |
| project_id | UUID |
| filename | VARCHAR |
| language | VARCHAR |
| original_code | TEXT |
| line_count | INTEGER |
| uploaded_at | TIMESTAMP |

---

## 4.4 Scan Jobs

Purpose

Tracks analysis executions.

Fields

| Column | Type |
|--------|------|
| id | UUID |
| project_id | UUID |
| started_at | TIMESTAMP |
| completed_at | TIMESTAMP |
| status | VARCHAR |

Status

- Pending
- Running
- Completed
- Failed

---

## 4.5 Scan Results

Purpose

Stores findings from static analysis and security tools.

Fields

| Column | Type |
|--------|------|
| id | UUID |
| scan_job_id | UUID |
| file_id | UUID |
| tool | VARCHAR |
| severity | VARCHAR |
| category | VARCHAR |
| line_number | INTEGER |
| message | TEXT |
| recommendation | TEXT |

Severity

- Critical
- High
- Medium
- Low
- Info

Tools

- Flake8
- Pylint
- Radon
- Bandit
- Semgrep
- detect-secrets
- pip-audit

---

## 4.6 AI Reviews

Purpose

Stores AI-generated explanations and fixes.

Fields

| Column | Type |
|--------|------|
| id | UUID |
| scan_result_id | UUID |
| explanation | TEXT |
| fixed_code | TEXT |
| reasoning | TEXT |
| model | VARCHAR |
| created_at | TIMESTAMP |

---

## 4.7 Reports

Purpose

Stores generated review reports.

Fields

| Column | Type |
|--------|------|
| id | UUID |
| project_id | UUID |
| report_type | VARCHAR |
| file_path | VARCHAR |
| generated_at | TIMESTAMP |

Report Types

- PDF
- HTML
- Markdown
- JSON

---

# 5. ChromaDB Collections

The vector database stores semantic representations of secure coding knowledge.

Collections

```

knowledge_chunks

```

Metadata

```

Source

Title

Language

Topic

OWASP Category

Section

```

---

# 6. Knowledge Chunk Structure

Example

```

{

"text": "...SQL Injection occurs...",

"metadata": {

"source":"OWASP",

"title":"SQL Injection",

"language":"Python",

"topic":"Injection",

"category":"OWASP A03"

}

}

```

---

# 7. Relationships

```

Users

1

↓

N

Projects

1

↓

N

CodeFiles

1

↓

N

ScanJobs

1

↓

N

ScanResults

1

↓

1

AIReviews

Projects

1

↓

N

Reports

```

---

# 8. Database Normalization

The relational schema follows Third Normal Form (3NF):

- No repeating groups
- Atomic values
- Elimination of partial dependencies
- Elimination of transitive dependencies

Benefits

- Reduced redundancy
- Improved consistency
- Easier maintenance

---

# 9. Indexing Strategy

Recommended indexes:

Projects

- project_name
- user_id

Code Files

- project_id
- language

Scan Results

- severity
- category
- tool

AI Reviews

- scan_result_id

Knowledge Chunks

- metadata fields

---

# 10. Data Flow

```

User Upload

↓

Projects

↓

CodeFiles

↓

ScanJob

↓

Static Analysis

↓

ScanResults

↓

AI Reviews

↓

Report

```

---

# 11. Security Considerations

Sensitive information

- Passwords
- API Keys
- Tokens

Protection

- bcrypt password hashing
- JWT Authentication
- HTTPS
- Least privilege
- Database backups
- Audit logging

---

# 12. Future Database Enhancements

Future versions may include:

- GitHub repositories
- Pull Request history
- Team workspaces
- Organization support
- Historical scan analytics
- AI conversation history
- User feedback on AI suggestions
- Model version tracking

---

# 13. Conclusion

The database design separates transactional application data (PostgreSQL) from semantic knowledge (ChromaDB). This hybrid architecture enables efficient storage of structured scan results while supporting semantic retrieval for Retrieval-Augmented Generation (RAG).

The schema is modular, scalable, and aligned with the multi-agent architecture of the AI Code Review & Security Analysis Agent.

---

# References

1. PostgreSQL Documentation
2. SQLAlchemy Documentation
3. ChromaDB Documentation
4. LangChain Documentation
5. OWASP ASVS
6. NIST Secure Software Development Framework