def project_profile_prompt(description: str) -> str:
    return f"""
You are an expert cloud solution architect.

Extract a structured project profile from the following description.

Rules:
- Output ONLY valid JSON
- Do NOT add explanations
- Do NOT wrap in markdown
- If a field is missing, use null or empty list
- Budget must be a number (INR per month)

Required JSON format:
{{
  "name": string,
  "budget_inr_per_month": number,
  "description": string,
  "tech_stack": {{
    "frontend": string | null,
    "backend": string | null,
    "database": string | null,
    "storage": string | null,
    "monitoring": string | null,
    "hosting": string | null
  }},
  "non_functional_requirements": [string]
}}

Project description:
\"\"\"
{description}
\"\"\"
"""


def billing_generation_prompt(project_profile: dict) -> str:
    return f"""
You are a cloud cost simulation engine.

Using the project profile below, generate realistic synthetic cloud billing data.

Rules:
- Output ONLY valid JSON array
- Do NOT return code.
- Do NOT return markdown.
- Do NOT add explanations.
- 12 to 20 records
- Monthly costs must roughly respect the project budget
- Use realistic cloud services (compute, database, storage, networking, monitoring)
- Include region and usage details
- Cloud-agnostic (AWS / Azure / GCP allowed)

Each record format:
{{
  "month": "YYYY-MM",
  "service": string,
  "resource_id": string,
  "region": string,
  "usage_type": string,
  "usage_quantity": number,
  "unit": string,
  "cost_inr": number,
  "desc": string
}}

Project profile:
{project_profile}
"""


def cost_analysis_prompt(project_profile: dict, billing_data: list) -> str:
    return f"""
You are a cloud cost optimization expert.

Analyze the billing data and generate a cost optimization report.

Rules:
- Output ONLY valid JSON
- Do NOT return code.
- Do NOT return markdown.
- Provide 6 to 10 recommendations
- Recommendations must include AWS, Azure, GCP, and open-source options
- Include savings, risks, and implementation effort

Required JSON format:
{{
  "project_name": string,
  "analysis": {{
    "total_monthly_cost": number,
    "budget": number,
    "budget_variance": number,
    "service_costs": object,
    "is_over_budget": boolean
  }},
  "recommendations": [
    {{
      "title": string,
      "service": string,
      "current_cost": number,
      "potential_savings": number,
      "recommendation_type": string,
      "description": string,
      "implementation_effort": "low|medium|high",
      "risk_level": "low|medium|high",
      "cloud_providers": [string]
    }}
  ]
}}

Project profile:
{project_profile}

Billing data:
{billing_data}
"""
