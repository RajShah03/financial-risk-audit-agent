from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json
import re

load_dotenv()

llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile"
)

def structure_data(state):
    print("\n[DEBUG] Running LLM Structurer...")

    combined_text = " ".join(state["search_results"])

    prompt = f"""
You are a financial analyst AI.

From the financial information below, extract structured financial signals.

Text:
{combined_text}

Extract and return ONLY valid JSON in this format:

{{
    "profit_status": "positive/negative/mixed/unknown",
    "revenue_trend": "growing/declining/stable/unknown",
    "debt_level": "low/moderate/high/unknown",
    "overall_risk": "low/medium/high",
    "reasoning": "short explanation"
}}

Important:
- Consider latest financial signals.
- If company was loss-making before but now profitable, mark as "positive".
- If information unclear, use "unknown".
- Do not hallucinate numbers.
- Return JSON only.
"""

    response = llm.invoke(prompt)

    raw_text = response.content.strip()

    # Extract JSON block using regex
    json_match = re.search(r"\{.*\}", raw_text, re.DOTALL)

    if json_match:
        try:
            parsed = json.loads(json_match.group())
            structured = parsed
        except Exception as e:
            print("[ERROR] JSON parsing failed:", e)
            structured = {
                "profit_status": "unknown",
                "revenue_trend": "unknown",
                "debt_level": "unknown",
                "overall_risk": "unknown",
                "reasoning": "Parsing failed"
            }
    else:
        print("[ERROR] No JSON found in LLM response")
        structured = {
            "profit_status": "unknown",
            "revenue_trend": "unknown",
            "debt_level": "unknown",
            "overall_risk": "unknown",
            "reasoning": "No JSON found"
        }

    state["structured_data"] = structured
    return state