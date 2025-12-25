# ☁️ Cloud Cost Optimizer

A **CLI-based intelligent cloud cost analysis and optimization tool** powered by Large Language Models (LLMs).
This project takes a natural language project description, extracts a structured cloud profile, generates **realistic synthetic billing data**, and produces **actionable cost optimization recommendations** across AWS, Azure, GCP, and open‑source alternatives.

---

## 🚀 Key Features

* 🧠 **LLM-powered project understanding** from plain English
* 📊 **Synthetic cloud billing generation** (realistic + budget-aware)
* 💡 **Cost optimization recommendations** with savings, risks & effort
* 🧱 Clean **modular pipeline architecture**
* 🖥️ Simple **CLI interface**
* 🔒 Strict **JSON-only outputs** for reliability
---

## 🎥 Demo Video

A short demo video demonstrating the complete working of the **Cloud Cost Optimizer CLI**, including project profiling, billing generation, and cost optimization analysis:

👉 **Project Demo Video (Google Drive – MP4):**  
https://drive.google.com/file/d/1S1FpjmvOoAACM7PeFHFHXWkjCWCVHJH3/view

---

## 🏗️ Project Architecture

```
cloud-cost-optimizer/
│
├── main.py                     # Entry point (CLI)
├── data/
│   ├── input/
│   │   └── project_description.txt
│   └── output/
│       ├── project_profile.json
│       ├── mock_billing.json
│       └── cost_analysis.json
│
├── src/
│   ├── cli/
│   │   └── menu.py              # CLI menu logic
│   ├── pipeline/
│   │   ├── profile_extractor.py
│   │   ├── billing_generator.py
│   │   └── cost_analyzer.py
│   ├── llm/
│   │   ├── hf_client.py          # Hugging Face API client
│   │   └── prompts.py            # All LLM prompts
│   └── utils/
│       └── file_handler.py       # JSON / text file helpers
│
└── requirements.txt
```

---

## 🧠 How It Works (Pipeline Flow)

1. **Project Description**
   User writes a natural language description in `project_description.txt`

2. **Project Profiling**
   LLM extracts structured cloud requirements → `project_profile.json`

3. **Billing Simulation**
   LLM generates realistic monthly billing data → `mock_billing.json`

4. **Cost Analysis**
   LLM analyzes costs & suggests optimizations → `cost_analysis.json`

---

## 📦 Prerequisites

* Python **3.10+**
* Git
* Hugging Face account + API token

---

## 🛠️ Setup Instructions (Step-by-Step)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mnkraj/AI-Powered-Cloud-Cost-Optimizer
cd cloud-cost-optimizer
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

```bash
HF_API_KEY=huggingface_api_token 
HF_MODEL =    #meta-llama/Meta-Llama-3-8B-Instruct:novita
HF_API_BASE_URL = #https://router.huggingface.co/v1/chat/completions

```

---

### 4️⃣ Add Project Description

Edit:

```
data/input/project_description.txt
```

Example:

```
A web-based placement portal for a university where students can log in using institute email IDs,
view company hiring details, and track applications. The system should be low-cost and scalable.
```

---

## ▶️ Running the Application

```bash
python main.py
```

You will see a menu:

```
1. Enter new project description
2. Extract Project Profile
3. Generate mock billing data
4. Generate cost optimization report
5. Exit
```

---

## 📂 Output Files

| File                   | Description                     |
| ---------------------- | ------------------------------- |
| `project_profile.json` | Structured cloud requirements   |
| `mock_billing.json`    | Synthetic cloud billing records |
| `cost_analysis.json`   | Optimization recommendations    |

All files are located in:

```
data/output/
```

---

## 🔐 Design Guarantees

* ❌ No markdown in LLM outputs
* ❌ No code generation in data stages
* ❌ No malformed JSON
* ✅ Strict schema validation
* ✅ Deterministic, pipeline-safe prompts

---

## 🧪 Testing Tips

* Try **short vs long descriptions**
* Try **low vs high budget projects**
* Run steps individually or full pipeline
* Inspect JSON outputs manually

---

## 🌱 Future Enhancements

* JSON Schema validation
* Retry & fallback LLM logic
* CSV / Excel export
* Cost trend visualization
* Real cloud billing ingestion
* Web UI / Dashboard

---

## 🏗️ Project Architecture

