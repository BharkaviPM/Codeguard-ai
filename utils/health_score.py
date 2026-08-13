class HealthScore:

    @staticmethod
    def calculate(
        high,
        medium,
        low
    ):

        score = (
            100
            - (high * 15)
            - (medium * 7)
            - (low * 3)
        )

        return max(score, 0)