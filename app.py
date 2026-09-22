from graph.workflow import graph

query = """
Provide intelligence on Pembrolizumab
including clinical trial status,
regulatory developments,
and competitor landscape.
"""

result = graph.invoke(
    {
        "query": query,
        "clinical_context": [],
        "regulatory_context": [],
        "competitive_context": [],
        "clinical_findings": "",
        "regulatory_findings": "",
        "competitive_findings": "",
        "validation_result": "",
        "impact_score": "",
        "final_report": ""
    }
)

print(result["final_report"])