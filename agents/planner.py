def create_plan(state):
    user_query = state["user_query"]

    # Extract clean company name
    company = user_query.replace("Audit", "").replace("IPO", "").strip()

    state["plan"] = [
        f"{company} company overview and business model",
        f"{company} FY2025 revenue net profit PAT total debt balance sheet financial numbers",
        f"{company} latest quarterly results revenue growth profit margin",
        f"{company} total liabilities and borrowings latest data",
        f"{company} major competitors market share",
        f"{company} financial risks going concern warnings losses debt issues"
    ]

    return state