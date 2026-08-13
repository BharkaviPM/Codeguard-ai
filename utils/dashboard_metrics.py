# utils/dashboard_metrics.py

import re


class DashboardMetrics:

    @staticmethod
    def calculate(*texts):

        content = "\n".join(
            [str(x) for x in texts if x]
        ).lower()

        high = len(
            re.findall(r"\bhigh\b", content)
        )

        medium = len(
            re.findall(r"\bmedium\b", content)
        )

        low = len(
            re.findall(r"\blow\b", content)
        )

        total = high + medium + low

        if total == 0:
            score = 100
        else:
            penalty = (
                high * 15 +
                medium * 8 +
                low * 3
            )

            score = max(
                0,
                100 - penalty
            )

        return {
            "high": high,
            "medium": medium,
            "low": low,
            "health_score": score
        }