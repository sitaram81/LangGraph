# Database Checkpointer Example

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph, START, END

graph= StateGraph()
# save state to a SQLite database
checkpointer = SqliteSaver(db_path="graph_checkpoints.db")
compiled_graph = graph.compile(checkpointer=checkpointer)
thread_id = "student_chat_2"
result = compiled_graph.invoke({"input": "Hello!"}, thread_id=thread_id)
