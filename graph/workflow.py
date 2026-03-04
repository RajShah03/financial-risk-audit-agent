from langgraph.graph import StateGraph, END
from state import AgentState

from agents.intent import detect_intent
from agents.planner import create_plan
from agents.researcher import research
from agents.structurer import structure_data
from engine.risk_engine import apply_risk_engine
from agents.reporter import generate_report

def build_graph():
    
    workflow = StateGraph(AgentState)
    
    workflow.add_node("intent",detect_intent)
    workflow.add_node("planner",create_plan)
    workflow.add_node("researcher",research)
    workflow.add_node("structurer",structure_data) 
    workflow.add_node("risk_engine",apply_risk_engine)
    workflow.add_node("reporter",generate_report)
    
    workflow.set_entry_point("intent") 
    
    workflow.add_edge("intent","planner")
    workflow.add_edge("planner","researcher")
    workflow.add_edge("researcher","structurer")
    workflow.add_edge("structurer","risk_engine")
    workflow.add_edge("risk_engine","reporter")
    workflow.add_edge("reporter",END)
    
    return workflow.compile()
    