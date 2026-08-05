import re


class JavaAnalyzer:

    @staticmethod
    def analyze(code):

        findings = []

        if "System.out.println" in code:

            findings.append({

                "agent": "Code Analysis",

                "severity": "Low",

                "title": "Console Logging",

                "description":
                "Avoid System.out.println() in production.",

                "line_number": 1,

                "suggestion":
                "Use a logging framework."
            })

        methods = re.findall(

            r'public\s+\w+\s+\w+\(.*?\)',

            code

        )

        if len(methods) > 20:

            findings.append({

                "agent": "Code Analysis",

                "severity": "Medium",

                "title": "Large Class",

                "description":
                "Too many public methods.",

                "line_number": 1,

                "suggestion":
                "Split into multiple classes."
            })

        return findings