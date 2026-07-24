
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str):
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """

    print(f"searching for {query}")
    return tavily.search(query=query)

# llm = ChatOpenAI
llm = ChatOllama(model="qwen2.5:7b")
tools = [search]
agent = create_agent(model=llm,tools=tools)

def main():
    print("Hello from langchain-lab!")
    result = agent.invoke({"messages": HumanMessage(content="What is the weather in Tokyo?")})
    print(result)

if __name__ == "__main__":
    main()
