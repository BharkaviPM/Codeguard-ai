# OWASP Top 10 (2021) Notes

## 1. Introduction

The Open Worldwide Application Security Project (OWASP) is a non-profit organization dedicated to improving software security. The OWASP Top 10 is an industry-recognized list of the most critical web application security risks. It serves as a guideline for developers, security professionals, and organizations to identify, prevent, and mitigate common vulnerabilities during software development.

The AI Code Review & Security Analysis Agent uses OWASP guidelines as the primary knowledge source for detecting vulnerabilities, generating remediation suggestions, and providing secure coding recommendations.

---

# 2. OWASP Top 10 (2021)

| ID | Category | Description |
|----|----------|-------------|
| A01 | Broken Access Control | Unauthorized access due to improper authorization checks |
| A02 | Cryptographic Failures | Weak or missing encryption |
| A03 | Injection | SQL, Command, LDAP, NoSQL injections |
| A04 | Insecure Design | Missing security-by-design principles |
| A05 | Security Misconfiguration | Default credentials, exposed services, insecure settings |
| A06 | Vulnerable Components | Outdated dependencies with known vulnerabilities |
| A07 | Identification & Authentication Failures | Weak authentication and session management |
| A08 | Software & Data Integrity Failures | Supply chain attacks, insecure updates |
| A09 | Security Logging & Monitoring Failures | Insufficient logging and monitoring |
| A10 | Server-Side Request Forgery (SSRF) | Server requests internal or external resources unsafely |

---

# 3. SQL Injection (OWASP A03)

## Description

SQL Injection occurs when user input is directly concatenated into SQL queries without validation or parameterization.

## Vulnerable Example (Python)

```python
username = input("Username: ")

query = f"SELECT * FROM users WHERE username='{username}'"
```

# If the attacker enters:

' OR '1'='1

# The query becomes:

SELECT * FROM users
WHERE username='' OR '1'='1'

This may return all user records.

# Secure Example
cursor.execute(
    "SELECT * FROM users WHERE username=%s",
    (username,)
)
Prevention
Prepared Statements
Parameterized Queries
Input Validation
# Least Privilege Database Accounts
4. Cross-Site Scripting (XSS)
Description

Cross-Site Scripting allows attackers to inject malicious JavaScript into web pages viewed by other users.

# Vulnerable Example
<div>{{ user_comment }}</div>

If not escaped:

<script>alert("Hacked")</script>
Prevention
Output Encoding
HTML Escaping
Content Security Policy (CSP)
Input Sanitization

5. Cross-Site Request Forgery (CSRF)
Description

CSRF tricks authenticated users into executing unwanted actions.

Prevention
CSRF Tokens
SameSite Cookies
Origin Validation
Double Submit Cookies

6. Server-Side Request Forgery (SSRF)
Description

An attacker forces the server to send requests to unintended destinations.

# Example:

requests.get(user_url)

If user_url is:

http://169.254.169.254/latest/meta-data

Cloud metadata may be exposed.

Prevention
Allowlists
Network Segmentation
URL Validation
Disable Redirects

7. Command Injection
Description

Occurs when untrusted input is passed to operating system commands.

Vulnerable Example
os.system("ping " + user_ip)
Prevention
Avoid shell=True
Use subprocess safely
Validate input
Least privilege

8. Broken Authentication

# Examples

Weak Passwords
Password Reuse
Missing MFA
Predictable Session IDs
Prevention
Strong Password Policies
MFA
Secure Session Cookies
Account Lockout

9. Security Misconfiguration

# Examples

Default Passwords
Open Debug Mode
Directory Listing
Public Cloud Buckets
Prevention
Secure Defaults
Disable Debug Mode
Regular Security Audits

10. Cryptographic Failures

# Examples

MD5
SHA1
Plain Text Password Storage
Prevention
bcrypt
Argon2
PBKDF2
TLS 1.2+

11. Vulnerable Components

# Examples

Outdated Python Packages
Vulnerable Java Libraries

Detection Tools

pip-audit
OWASP Dependency Check

12. Logging & Monitoring Failures

# Examples

Missing Audit Logs
No Failed Login Logs
No Alerting

Best Practices

Centralized Logging
SIEM Integration
Audit Trails

13. Secure Coding Checklist
Validate all user input
Use parameterized queries
Escape HTML output
Hash passwords securely
Protect secrets
Use HTTPS
Apply least privilege
Enable logging
Keep dependencies updated
Perform regular security scans

14. How This Project Uses OWASP

The AI Code Review & Security Analysis Agent will utilize OWASP standards as the foundation for its Security Vulnerability Agent.

The Security Agent will:

Detect SQL Injection
Detect Command Injection
Detect Hardcoded Secrets
Detect XSS
Detect SSRF
Detect Weak Authentication
Detect Security Misconfiguration
Map findings to OWASP Top 10 categories
Assign severity levels (Critical, High, Medium, Low)
Generate remediation recommendations

The knowledge contained in this document will also be indexed into the Retrieval-Augmented Generation (RAG) knowledge base to support the Conversational Code Assistant.