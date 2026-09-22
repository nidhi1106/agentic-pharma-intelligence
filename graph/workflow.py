from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import PharmaState

from agents.supervisor import supervisor_node
from agents.clinical_agent import clinical_agent
from agents.regulatory_agent import regulatory_agent
from agents.competitive_agent import competitive_agent
from agents.validation_agent import validation_agent
from agents.scoring_agent import scoring_agent
from agents.summary_agent import summary_agent


builder = StateGraph(PharmaState)

builder.add_node("supervisor", supervisor_node)

builder.add_node("clinical", clinical_agent)
builder.add_node("regulatory", regulatory_agent)
builder.add_node("competitive", competitive_agent)

builder.add_node("validation", validation_agent)
builder.add_node("scoring", scoring_agent)
builder.add_node("summary", summary_agent)

builder.set_entry_point("supervisor")

builder.add_edge(
    "supervisor",
    "clinical"
)

builder.add_edge(
    "clinical",
    "regulatory"
)

builder.add_edge(
    "regulatory",
    "competitive"
)

builder.add_edge(
    "competitive",
    "validation"
)

builder.add_edge(
    "validation",
    "scoring"
)

builder.add_edge(
    "scoring",
    "summary"
)

builder.add_edge(
    "summary",
    END
)

graph = builder.compile()