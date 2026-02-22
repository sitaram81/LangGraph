from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  

llm = ChatOpenAI()

# Create message schema
class ChatState(TypedDict):
    message: Annotated[list[BaseMessage], add_messages]

# Create function to execute LLM
def Chat_node(state: ChatState) -> ChatState:
    message = state["message"]
    response = llm.invoke(message)
    return {"message": [response]}
# Check pointer
checkpointer = InMemorySaver()
# graph object
graph= StateGraph(ChatState)
# graph nodes and edges
graph.add_node('chat_node', Chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)
# graph compile
chatbot=graph.compile(checkpointer=checkpointer)
