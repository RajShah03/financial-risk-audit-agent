def apply_risk_engine(state):
    structured_data = state.get("structured_data", {})
    
    score = 0
    reasons = []

    if structured_data.get("profit_status") == "negative":
        score += 20
        reasons.append("Company is not profitable")

    if structured_data.get("debt_level") == "high":
        score += 25
        reasons.append("High debt levels")

    if structured_data.get("revenue_growth") == "declining":
        score += 15
        reasons.append("Revenue growth is declining")

    state["risk_score"] = score
    state["risk_reasoning"] = reasons

    return state