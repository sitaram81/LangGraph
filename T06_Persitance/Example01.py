from langgraph.checkpoint.memory import Memorysaver
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI 

# Define a simple graph
graph = StateGraph()

# Add persistence with a checkpointer
checkpointer = Memorysaver()
compiled_graph = graph.compile(checkpointer=checkpointer)

# Run the graph with persistence
thread_id = "student_chat_1"
result = compiled_graph.invoke({"input": "Hello!"}, thread_id=thread_id)

# Later, resume the same thread
result2 = compiled_graph.invoke({"input": "How are you?"}, thread_id=thread_id)

"""
Here:
	• MemorySaver acts as the checkpointer.
	• thread_id ensures all checkpoints are tied to the same conversation.
	• You can stop and restart, and the chatbot will still remember the earlier context.
	
Key Takeaways
	• Persistence = Saving graph state with checkpoints.
	• Threads = Organize checkpoints for continuity.
	• Benefits = Memory, fault tolerance, time travel, human-in-the-loop.
Practical Example = Chatbots, workflows, or AI agents that need to remember past runs.
"""