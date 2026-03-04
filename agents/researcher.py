from tools.web_search import web_search

def research(state):
    results = []

    for step in state["plan"]:
        search_data = web_search(step)
        print("\n[DEBUG] Raw Tavily Results For Step:", step)
        for r in search_data:
            print("-", r[:200], "...")  # print first 200 chars
        results.extend(search_data)

    state["search_results"] = results
    return state