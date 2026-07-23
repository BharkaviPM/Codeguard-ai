from collections import Counter


class SeverityEngine:

    @staticmethod
    def summarize(findings):

        counter = Counter()

        for finding in findings:

            counter[finding.severity.value] += 1

        return {

            "critical": counter["CRITICAL"],

            "high": counter["HIGH"],

            "medium": counter["MEDIUM"],

            "low": counter["LOW"],

            "info": counter["INFO"]

        }