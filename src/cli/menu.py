from src.pipeline.profile_extractor import extract_project_profile
from src.pipeline.billing_generator import generate_mock_billing
from src.pipeline.cost_analyzer import generate_cost_report
from src.utils.file_handler import write_json, read_text
import json
import os


def show_menu():
    while True:
        print("\n=== Cloud Cost Optimizer ===")
        print("1. Enter new project description")
        print("2. Extract Project Profile")
        print("3. Generate mock billing data")
        print("4. Generate cost optimization report")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == "1":
            handle_project_description()

        elif choice == "2":
            extract_project_profile()

        elif choice == "3":
            generate_mock_billing()

        elif choice == "4":
            generate_cost_report()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")



def handle_project_description():
    print("\nEnter your project description (end with an empty line):")
    lines = []

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    description = "\n".join(lines)

    os.makedirs("data/input", exist_ok=True)
    with open("data/input/project_description.txt", "w", encoding="utf-8") as f:
        f.write(description)

    print("✅ Project description saved to data/input/project_description.txt")



def view_recommendations():
    path = "data/output/cost_optimization_report.json"

    if not os.path.exists(path):
        print("❌ No report found. Run analysis first.")
        return

    with open(path, "r", encoding="utf-8") as f:
        report = json.load(f)

    print("\n=== Recommendations ===")
    for idx, rec in enumerate(report.get("recommendations", []), 1):
        print(f"\n{idx}. {rec['title']}")
        print(f"   Service: {rec['service']}")
        print(f"   Potential Savings: ₹{rec['potential_savings']}")
        print(f"   Providers: {', '.join(rec['cloud_providers'])}")
