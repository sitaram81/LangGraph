#MemorySaver Example

from langgraph.checkpoint.memory import Memorysaver
from langgraph.graph import StateGraph, START, END

graph = StateGraph()
checkpointer = Memorysaver()

compiled_graph = graph.compile(checkpointer=checkpointer)
thread_id = "student_chat_1"
result = compiled_graph.invoke({"input": "Hello!"}, thread_id=thread_id)
