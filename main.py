from dotenv import load_dotenv
load_dotenv()

from graph.workflow import build_graph

if __name__ == "__main__":
    graph = build_graph()
    
    user_query = input("Enter company or IPO to audit: ")
    
    initial_state = {
        "user_query": user_query,
        "intent": "",
        "plan": [],
        "search_results": [],
        "structured_data": [],
        "risk_score": 0,
        "risk_resoning": [],
        "final_report": ""
    }
    
    result = graph.invoke(initial_state)
    
    print("\n\n===== FINAL REPORT =====\n")
    print(result["final_report"])