from app.agents.analysis.agent import AnalysisAgent


class CoordinatorAgent:

    def __init__(self):

        self.analysis_agent = AnalysisAgent()

    def analyze(
        self,
        project_path: str,
        language: str,
    ):

        return self.analysis_agent.analyze(
            project_path=project_path,
            language=language,
        )