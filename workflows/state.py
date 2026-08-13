from typing import TypedDict


class ReviewState(TypedDict):

    code: str

    security_review: str

    code_review: str

    remediation: str

    summary: str