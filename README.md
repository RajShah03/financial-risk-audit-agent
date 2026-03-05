Title :- Autonomous Market Research & Risk Audit Agent

Description :- An AI-powered agent that autonomously researches companies and performs financial risk analysis. 
The system uses LLMs and external tools to gather information, analyze financial indicators, 
and generate an investment verdict such as Buy, Hold, or Avoid.

Features :- 
- Accepts a company or IPO name as input
- Collects financial and market information using web search APIs
- Performs structured analysis of company fundamentals
- Generates a risk score and investment verdict
- Built using an agentic workflow architecture

Tech Stack :-
- Python
- LangGraph
- Groq API
- Tavily Search API
- LangChain

Architecture :-
Workflow

User Input → Research Agent → Financial Analysis → Risk Scoring → Final Verdict

Output :-
Input: Tata Motors

Revenue Growth: Strong
Debt Level: Moderate
Market Sentiment: Positive

Risk Score: 6.5 / 10
Verdict: ACCUMULATE

How To Run:-

1. Clone the repository
2. Install dependencies
3. Add API keys in .env file
4. Run:

python main.py


