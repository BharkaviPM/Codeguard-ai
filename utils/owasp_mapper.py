class OWASPMapper:

    MAPPING = {

        "sql injection":
        "A03:2021 Injection",

        "xss":
        "A03:2021 Injection",

        "csrf":
        "A01:2021 Broken Access Control",

        "hardcoded secret":
        "A02:2021 Cryptographic Failures",

        "ssrf":
        "A10:2021 SSRF"
    }

    @staticmethod
    def map(text):

        text = text.lower()

        findings = []

        for key, value in (
            OWASPMapper.MAPPING.items()
        ):

            if key in text:

                findings.append(value)

        return list(
            set(findings)
        )