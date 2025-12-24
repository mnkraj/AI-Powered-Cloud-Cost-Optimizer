def project_profile_prompt(description: str) -> str:
    return f"""
SYSTEM ROLE:
You are a deterministic information extraction engine.
You do NOT explain, reason aloud, or generate examples.
You ONLY extract structured data.

TASK:
Convert the given project description into a STRICTLY VALID JSON object.

ABSOLUTE OUTPUT RULES (NON-NEGOTIABLE):
- Output MUST be valid JSON
- Output MUST start with {{ and end with }}
- Do NOT include markdown, code blocks, comments, or explanations
- Do NOT include trailing commas
- Do NOT invent technologies not implied by the description
- Do NOT include additional keys beyond the defined schema

DATA NORMALIZATION RULES:
- If a value is missing or unclear, use null (not empty string)
- If a list has no items, return []
- Budget MUST be a numeric value representing INR per month
- If budget is not mentioned, estimate conservatively based on project scale

SCHEMA (FOLLOW EXACTLY):
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

VALIDATION CHECK BEFORE RESPONDING:
- Is the output valid JSON?
- Are all required keys present?
- Are all values using correct data types?

PROJECT DESCRIPTION (SOURCE OF TRUTH):
\"\"\"
{description}
\"\"\"
"""

def billing_generation_prompt(project_profile: dict) -> str:
    return f"""
SYSTEM ROLE:
You are a cloud billing data generator.
You generate DATA, not code, not explanations.

TASK:
Generate realistic synthetic cloud billing records based on the provided project profile.

ABSOLUTE OUTPUT RULES (NON-NEGOTIABLE):
- Output MUST be a valid JSON ARRAY
- Output MUST start with [ and end with ]
- Do NOT include markdown
- Do NOT include code
- Do NOT include comments or explanations
- Do NOT wrap output in quotes
- Do NOT reference how the data was generated

DATA CONSTRAINTS:
- Generate between 12 and 20 records
- Each record represents a monthly billing item
- Total monthly cost should be close to (but not wildly exceed) the budget
- Costs must be realistic and non-negative
- Use cloud services from AWS, Azure, or GCP only
- Regions must be realistic cloud regions
- Usage units must match usage type

ALLOWED USAGE TYPES:
Compute, Storage, Database, Networking, Monitoring

SCHEMA (FOLLOW EXACTLY):
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

VALIDATION CHECK BEFORE RESPONDING:
- Is the output valid JSON?
- Is the output an array?
- Are there 12–20 objects?
- Does every object match the schema exactly?

PROJECT PROFILE (READ-ONLY INPUT):
{project_profile}
"""

def cost_analysis_prompt(project_profile: dict, billing_data: list) -> str:
    return f"""
SYSTEM ROLE:
You are a cloud cost optimization analyst.
You produce structured analytical output only.

TASK:
Analyze the provided billing data and generate a cost optimization report.

ABSOLUTE OUTPUT RULES (NON-NEGOTIABLE):
- Output MUST be valid JSON
- Do NOT include markdown
- Do NOT include code
- Do NOT include explanations outside JSON
- Do NOT invent billing data
- Use ONLY the provided inputs

ANALYSIS RULES:
- total_monthly_cost must be the sum of all billing records
- budget must match project_profile budget
- budget_variance = budget - total_monthly_cost
- is_over_budget must be logically correct

RECOMMENDATION RULES:
- Provide 6 to 10 recommendations
- Include AWS, Azure, GCP, AND open-source options overall
- Savings must be realistic and <= current_cost
- Risks and effort must be justified
- Avoid generic advice

SCHEMA (FOLLOW EXACTLY):
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

VALIDATION CHECK BEFORE RESPONDING:
- Is output valid JSON?
- Are numeric fields numbers (not strings)?
- Are enums strictly followed?

PROJECT PROFILE:
{project_profile}

BILLING DATA:
{billing_data}
"""
