from langgraph.checkpoint import MemorySaver
from langgraph.graph import StateGraph

graph = StateGraph()
checkpointer = MemorySaver()
compiled_graph = graph.compile(checkpointer=checkpointer)

# Start a new thread
thread_id = "student_session_001"
compiled_graph.invoke({"input": "Hello!"}, thread_id=thread_id)

# Continue the same thread
compiled_graph.invoke({"input": "Tell me about LangGraph."}, thread_id=thread_id)