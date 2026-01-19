import requests
import json
import os
from prompt import SYSTEM_PROMPT  # your prompt file

# ----------------------------
# Config
# ----------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"
OUTPUT_FOLDER = "sample_outputs"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ----------------------------
# Functions
# ----------------------------
def get_input():
    return (
        input("Enter company name: "),
        input("Enter industry: "),
        input("Enter target audience: "),
        input("Enter tone (professional/friendly/marketing): ")
    )

def build_prompt(company, industry, audience, tone):
    return SYSTEM_PROMPT + f"""
Company Name: {company}
Industry: {industry}
Target Audience: {audience}
Tone: {tone}
"""

def generate(prompt):
    try:
        res = requests.post(
            OLLAMA_URL,
            headers={"Content-Type": "application/json"},
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=60
        )
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def save_json(company, data):
    filename = f"{OUTPUT_FOLDER}/{company.replace(' ', '_')}_brochure.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data.get("response", {}), f, indent=4, ensure_ascii=False)
    return filename

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    company, industry, audience, tone = get_input()
    prompt = build_prompt(company, industry, audience, tone)
    result = generate(prompt)

    if "response" in result:
        print("\nGENERATED BROCHURE:\n")
        print(result["response"])
    else:
        print("\nERROR OR RAW RESPONSE:\n")
        print(result)

    saved_file = save_json(company, result)
    print(f"\nBrochure saved to: {saved_file}")
