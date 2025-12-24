import json
from src.llm.hf_client import call_llm
from src.llm.prompts import billing_generation_prompt
from src.utils.file_handler import write_json , read_json


def generate_mock_billing(project_profile: dict| None = None):
    if project_profile is None:
        project_profile = read_json("data/output/project_profile.json")
    print("\nGenerating mock billing data...")
    print("Reading project profile from data/output/project_profile.json ...")
    prompt = billing_generation_prompt(project_profile)
    response = call_llm(prompt)
    try:
        billing = json.loads(response["content"])
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON for billing data")

    write_json("data/output/mock_billing.json", billing)
    print("✅ Mock billing data generated and saved to data/output/mock_billing.json")
    return billing
