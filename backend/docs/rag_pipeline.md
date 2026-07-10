# Retrieval-Augmented Generation (RAG) Pipeline

# 1. Introduction

Retrieval-Augmented Generation (RAG) is an AI architecture that combines information retrieval with Large Language Models (LLMs). Instead of relying only on the model's internal knowledge, RAG retrieves relevant documents from a knowledge base and provides them as context to the LLM before generating a response.

In the AI Code Review & Security Analysis Agent, the RAG pipeline enables the Conversational Code Assistant and Remediation Agent to provide accurate, explainable, and up-to-date guidance based on trusted secure coding resources.

---

# 2. Why RAG?

Traditional LLMs have several limitations:

- Limited knowledge after training
- Hallucinated answers
- No awareness of project-specific documents
- Difficult to update with new information

RAG solves these problems by retrieving relevant documents dynamically before generating responses.

---

# 3. RAG Architecture

```

Developer Question

↓

Query Processing

↓

Retriever

↓

ChromaDB

↓

Relevant Chunks

↓

Prompt Construction

↓

LLM (Ollama)

↓

Generated Answer

```

---

# 4. RAG Pipeline Workflow

The RAG pipeline in this project follows these stages:

1. Document Collection
2. Text Extraction
3. Chunking
4. Embedding Generation
5. Vector Storage
6. Similarity Search
7. Prompt Construction
8. LLM Response Generation

---

# 5. Document Collection

Knowledge sources include:

```

knowledge_base/

OWASP/

CERT/

CWE/

Python/

Java/

```

Examples:

- OWASP Top 10
- OWASP Cheat Sheets
- CERT Secure Coding Standard
- CWE Database
- Python Secure Coding Guide
- Java Secure Coding Guide
- Secure API Design Documents

---

# 6. Text Extraction

PDF documents are converted into text.

Library:

```

PyMuPDF (fitz)

```

Process:

PDF

↓

Extract Text

↓

Clean Formatting

↓

Store Raw Text

---

# 7. Chunking

Large documents are divided into smaller sections.

Purpose:

- Improve retrieval accuracy
- Reduce LLM context size
- Faster searches

Configuration

Chunk Size

```

500 words

```

Overlap

```

50 words

```

Example

Original

```

SQL Injection
...
(2000 words)

```

Becomes

```

Chunk 1

Chunk 2

Chunk 3

Chunk 4

```

---

# 8. Embeddings

Each chunk is converted into a numerical vector representation.

Embedding Models

Recommended:

```

nomic-embed-text

```

Alternative:

```

mxbai-embed-large

```

Served using

```

Ollama

```

Example

Text

```

SQL Injection occurs...

```

↓

Vector

```

[0.142,
0.983,
0.673,
...]

```

---

# 9. Vector Database

The project uses:

```

ChromaDB

```

Each chunk is stored with metadata.

Example Metadata

```

Source:
OWASP

Title:
SQL Injection

Language:
Python

Topic:
Injection

Category:
OWASP A03

```

---

# 10. Similarity Search

When a user asks a question, the query is converted into an embedding.

The retriever compares the query vector with stored vectors using cosine similarity.

Formula

```

Similarity = Cosine(Query, Chunk)

```

Higher similarity indicates more relevant documents.

Top K

```

5

```

The five most relevant chunks are retrieved.

---

# 11. Metadata Filtering

Metadata improves retrieval accuracy.

Examples

Retrieve only:

```

Language = Python

```

or

```

Category = OWASP A03

```

Example

Question

```

Explain SQL Injection in Python.

```

Retriever returns

- Python Secure Coding
- OWASP SQL Injection
- CWE-89

instead of Java documents.

---

# 12. Prompt Construction

The retrieved chunks are inserted into the prompt.

Example

```

System:

You are a secure coding expert.

Context:

[Retrieved Documents]

Question:

How do I fix SQL Injection?

```

The LLM answers using the retrieved context.

---

# 13. LLM

Recommended Local Models

- Llama 3
- CodeLlama
- DeepSeek Coder
- Qwen Coder

Served using

```

Ollama

```

Benefits

- Offline
- Private
- No API cost
- Fast local inference

---

# 14. Example Workflow

Developer asks

```

Why is my SQL query vulnerable?

```

Retriever

↓

OWASP SQL Injection

↓

Python Secure Coding

↓

CWE-89

↓

Prompt

↓

LLM

↓

Answer

```

Your code is vulnerable because it concatenates user input into SQL queries. Use parameterized queries instead...

```

---

# 15. RAG in This Project

The RAG pipeline supports:

## Conversational Code Assistant

Example Questions

- Explain this vulnerability.
- Why is this code insecure?
- Show secure Python code.
- Show secure Java code.
- Explain OWASP A01.
- Explain Cyclomatic Complexity.

---

## Remediation Agent

Provides

- Secure code examples
- Refactored implementations
- Best practice explanations
- References to OWASP and CERT

---

## PR Summary Agent

Uses retrieved documents to generate:

- Security recommendations
- Code quality improvements
- Compliance suggestions

---

# 16. Advantages

- Reduces hallucinations
- Provides explainable answers
- Uses trusted security documentation
- Easy to update
- Supports multiple languages
- Improves AI recommendations

---

# 17. Limitations

- Retrieval quality depends on embeddings
- Poor chunking reduces accuracy
- Large knowledge bases require indexing time
- Metadata quality affects filtering

---

# 18. Future Improvements

Future enhancements include:

- Hybrid Search (Keyword + Vector)
- Re-ranking Models
- GraphRAG
- Knowledge Graph Integration
- Incremental Index Updates
- Multi-language Knowledge Base
- Context-aware Retrieval
- Conversation Memory

---

# 19. Application in This Project

The RAG pipeline is central to the AI Code Review & Security Analysis Agent.

It will be used by:

- Conversational Code Assistant
- Remediation Agent
- PR Summary Agent

Knowledge Sources:

- OWASP
- CERT
- CWE
- Python Secure Coding
- Java Secure Coding
- Internal Project Documentation

The retrieved knowledge will enable the agents to generate accurate, explainable, and context-aware responses.

---

# 20. References

1. Lewis et al. (2020), Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
2. ChromaDB Documentation
3. LangChain Documentation
4. Ollama Documentation
5. OWASP Cheat Sheet Series
6. CERT Secure Coding Standards
7. CWE Database