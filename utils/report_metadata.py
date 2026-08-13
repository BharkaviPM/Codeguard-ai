from datetime import datetime


class ReportMetadata:

    @staticmethod
    def generate():

        return {
            "generated_at":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M"
            )
        }