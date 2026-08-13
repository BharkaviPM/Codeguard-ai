import re


class SeverityParser:

    @staticmethod
    def extract_counts(text):

        high = len(
            re.findall(
                r"\bHIGH\b",
                text.upper()
            )
        )

        medium = len(
            re.findall(
                r"\bMEDIUM\b",
                text.upper()
            )
        )

        low = len(
            re.findall(
                r"\bLOW\b",
                text.upper()
            )
        )

        return {
            "High": high,
            "Medium": medium,
            "Low": low
        }