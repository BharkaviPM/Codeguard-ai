from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib import colors

import re


class PDFGenerator:

    @staticmethod
    def clean_text(text):

        if not text:
            return ""

        # Remove markdown headings
        text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)

        # Remove bold markers
        text = text.replace("**", "")

        # Remove code fences
        text = text.replace("```python", "")
        text = text.replace("```", "")

        # Remove markdown tables
        cleaned_lines = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            if "|" in line:
                continue

            if "---" == line:
                continue

            cleaned_lines.append(line)

        return "\n".join(cleaned_lines)

    @staticmethod
    def generate(
        report_text,
        output_file="reports/code_review_report.pdf"
    ):

        doc = SimpleDocTemplate(output_file)

        styles = getSampleStyleSheet()

        title_style = styles["Title"]

        heading_style = ParagraphStyle(
            "HeadingStyle",
            parent=styles["Heading1"],
            textColor=colors.darkblue,
            spaceAfter=10
        )

        body_style = ParagraphStyle(
            "BodyStyle",
            parent=styles["BodyText"],
            leading=18,
            spaceAfter=5
        )

        story = []

        # Title
        story.append(
            Paragraph(
                "CodeGuard AI Enterprise Review Report",
                title_style
            )
        )

        story.append(Spacer(1, 20))

        sections = [
            "Executive Summary",
            "Security Analysis",
            "Code Quality Analysis",
            "Performance Analysis",
            "Risk Assessment",
            "Remediation Plan",
            "Dashboard"
        ]

        for i, section_name in enumerate(sections):

            start = report_text.find(section_name)

            if start == -1:
                continue

            if i < len(sections) - 1:
                end = report_text.find(
                    sections[i + 1],
                    start
                )

                if end == -1:
                    end = len(report_text)
            else:
                end = len(report_text)

            content = report_text[start:end]

            content = content.replace(
                section_name,
                "",
                1
            )

            content = PDFGenerator.clean_text(content)

            story.append(
                Paragraph(
                    section_name,
                    heading_style
                )
            )

            story.append(
                Spacer(1, 6)
            )

            paragraphs = content.split("\n")

            for para in paragraphs:

                para = para.strip()

                if not para:
                    continue

                story.append(
                    Paragraph(
                        para,
                        body_style
                    )
                )

            story.append(
                Spacer(1, 12)
            )

        doc.build(story)

        return output_file