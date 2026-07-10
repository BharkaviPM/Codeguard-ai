from pathlib import Path
import uuid

from app.core.config import settings


class WorkspaceManager:

    def create_workspace(self):

        project_id = str(uuid.uuid4())

        workspace = (
            Path(settings.WORKSPACE_DIR)
            / project_id
        )

        source = workspace / "source"

        analysis = workspace / "analysis"

        reports = workspace / "reports"

        source.mkdir(
            parents=True,
            exist_ok=True
        )

        analysis.mkdir(
            exist_ok=True
        )

        reports.mkdir(
            exist_ok=True
        )

        return {
            "project_id": project_id,
            "workspace": str(workspace)
        }