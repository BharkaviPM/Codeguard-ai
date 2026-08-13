import re


class SecurityScore:

    @staticmethod
    def calculate(text):

        text = text.lower()

        high = len(
            re.findall(
                r"high",
                text
            )
        )

        medium = len(
            re.findall(
                r"medium",
                text
            )
        )

        low = len(
            re.findall(
                r"low",
                text
            )
        )

        score = (
            100
            - (high * 15)
            - (medium * 8)
            - (low * 3)
        )

        return max(
            score,
            0
        )