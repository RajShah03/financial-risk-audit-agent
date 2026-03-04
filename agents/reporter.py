from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_report(state):
    prompt = f"""
    Generate a professional financial audit report.
    
    User Query: {state["user_query"]}
    
    Structured Data:
    {state["structured_data"]}
    
    Risk Score: {state["risk_score"]}
    Risk Reasons: {state["risk_reasoning"]}
    
    Provide:
    - Executive Summary
    - Financial Analysis
    - Risk Assessment
    - Final Verdict
    """
    
    response = llm.invoke(prompt)
    state["final_report"] = response.content
    
    return state