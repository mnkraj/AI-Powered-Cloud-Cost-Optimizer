import json
from src.llm.hf_client import call_llm
from src.llm.prompts import project_profile_prompt
from src.utils.file_handler import write_json, read_text


def extract_project_profile():
    print("\nExtracting project profile from data/input/project_description.txt ...")
    description = read_text("data/input/project_description.txt")

    prompt = project_profile_prompt(description)
    
    response = call_llm(prompt)


    try:
        profile = json.loads(response["content"])
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON for project profile")

    write_json("data/output/project_profile.json", profile)
    print("✅ Project profile extracted and saved to data/output/project_profile.json")
    return profile      