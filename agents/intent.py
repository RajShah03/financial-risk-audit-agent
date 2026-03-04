from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

def detect_intent(state):
    prompt = f"""
    Classify the user query into one of:
    - financial audit
    - general research
    
    Query: {state["user_query"]}
    
    Only return the label.
    """
    
    response = llm.invoke(prompt)
    state["intent"] = response.content.strip().lower()
    return state