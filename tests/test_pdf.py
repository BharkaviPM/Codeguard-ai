from reports.pdf_generator import PDFGenerator

PDFGenerator.generate(
    """
    Sample Report

    High Severity:
    SQL Injection

    Medium Severity:
    Error Handling
    """
)

print("PDF Generated")