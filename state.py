from typing import TypedDict,List,Dict

class AgentState(TypedDict):
    user_query : str
    intent : str
    plan : List[str]
    search_results : List[str]
    structured_data : Dict
    risk_score : float
    risk_reasoning : List[str]
    final_report : str