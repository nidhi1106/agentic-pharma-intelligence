from typing import TypedDict, List

class PharmaState(TypedDict):
    query: str

    clinical_context: List[str]
    regulatory_context: List[str]
    competitive_context: List[str]

    clinical_findings: str
    regulatory_findings: str
    competitive_findings: str

    validation_result: str
    impact_score: str
    final_report: str