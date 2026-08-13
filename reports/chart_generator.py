import matplotlib.pyplot as plt


class ChartGenerator:

    @staticmethod
    def create_chart():

        labels = [
            "Security",
            "Quality",
            "Maintainability",
            "Performance"
        ]

        values = [75, 80, 70, 85]

        plt.figure(figsize=(6,4))

        plt.bar(labels, values)

        plt.title(
            "Code Quality Metrics"
        )

        plt.savefig(
            "reports/quality_chart.png"
        )

        plt.close()