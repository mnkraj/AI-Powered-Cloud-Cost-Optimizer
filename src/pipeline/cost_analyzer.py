import json
from src.llm.hf_client import call_llm
from src.llm.prompts import cost_analysis_prompt
from src.utils.file_handler import write_json , read_json


def generate_cost_report(project_profile: dict | None = None, billing_data: list = None):
    if project_profile is None:
        project_profile = read_json("data/output/project_profile.json")
    if billing_data is None:
        billing_data = read_json("data/output/mock_billing.json")
    print("\nGenerating cost optimization report...")
    print("Reading project profile from data/output/project_profile.json ...")
    print("Reading mock billing data from data/output/mock_billing.json ...")
    prompt = cost_analysis_prompt(project_profile, billing_data)
    response = call_llm(prompt)
    try:
        report = json.loads(response["content"])
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON for cost report")

    write_json("data/output/cost_optimization_report.json", report)
    print("✅ Cost optimization report generated and saved to data/output/cost_optimization_report.json")
    return report
