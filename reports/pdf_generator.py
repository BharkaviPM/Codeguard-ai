from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib import colors


class PDFGenerator:

    @staticmethod
    def generate(
        report_text,
        output_file="reports/code_review_report.pdf"
    ):

        doc = SimpleDocTemplate(output_file)

        styles = getSampleStyleSheet()

        heading_style = ParagraphStyle(
            "Heading",
            parent=styles["Heading1"],
            textColor=colors.darkblue
        )

        body_style = styles["BodyText"]

        story = []

        story.append(
            Paragraph(
                "CodeGuard AI Review Report",
                styles["Title"]
            )
        )

        story.append(
            Spacer(1, 20)
        )

        story.append(
            Paragraph(
                "AI-Powered Security, Code Quality and Performance Review",
                body_style
            )
        )

        story.append(
            Spacer(1, 20)
        )

        sections = report_text.split("---")

        for section in sections:

            section = section.strip()

            if not section:
                continue

            lines = section.split("\n")

            heading = lines[0]

            body = "<br/>".join(lines[1:])

            story.append(
                Paragraph(
                    heading,
                    heading_style
                )
            )

            story.append(
                Spacer(1, 8)
            )

            story.append(
                Paragraph(
                    body,
                    body_style
                )
            )

            story.append(
                Spacer(1, 15)
            )

        doc.build(story)

        return output_file