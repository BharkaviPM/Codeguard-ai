from langgraph.graph import StateGraph
from langgraph.graph import END

from workflows.state import ReviewState

from agents.security_agent import SecurityAgent
from agents.code_analysis_agent import CodeAnalysisAgent
from agents.remediation_agent import RemediationAgent
from agents.summary_agent import SummaryAgent


# ----------------------------------
# NODES
# ----------------------------------

def security_node(state):

    state["security_review"] = (
        SecurityAgent.ai_review(
            state["code"]
        )
    )

    return state


def code_review_node(state):

    state["code_review"] = (
        CodeAnalysisAgent.ai_review(
            state["code"]
        )
    )

    return state


def remediation_node(state):

    state["remediation"] = (
        RemediationAgent.generate(
            state["code"],
            state["security_review"],
            state["code_review"]
        )
    )

    return state


def summary_node(state):

    state["summary"] = (
        SummaryAgent.generate(
            state["security_review"],
            state["code_review"],
            state["remediation"]
        )
    )

    return state


# ----------------------------------
# GRAPH
# ----------------------------------

builder = StateGraph(
    ReviewState
)

builder.add_node(
    "security",
    security_node
)

builder.add_node(
    "code_review",
    code_review_node
)

builder.add_node(
    "remediation",
    remediation_node
)

builder.add_node(
    "summary",
    summary_node
)

builder.set_entry_point(
    "security"
)

builder.add_edge(
    "security",
    "code_review"
)

builder.add_edge(
    "code_review",
    "remediation"
)

builder.add_edge(
    "remediation",
    "summary"
)

builder.add_edge(
    "summary",
    END
)

graph = builder.compile()