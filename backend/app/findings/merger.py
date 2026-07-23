from app.agents.analysis.models import Finding


class FindingsMerger:

    @staticmethod
    def merge(*groups):

        findings = []

        for group in groups:

            if isinstance(group, list):

                findings.extend(group)

            elif isinstance(group, dict):

                findings.extend(group.get("findings", []))

        return findings