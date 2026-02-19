from langgraph.graph import StateGraph,START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
#create a state
class LLMState(TypedDict):
    question: str
    answer: str

def llm_qa(state: LLMState) -> LLMState:
  #extract the question from state
  question=state['question']
  #create a prompt
  prompt=f"Answer the following question concisely: {question}"
  #ask the question to the LLM
  answer= model.invoke(prompt).content
  state['answer']=answer
  return state 

model=ChatOpenAI()

#create our graph
graph = StateGraph(LLMState)

#add nodes
graph.add_node('llm_qa', llm_qa)

#add edges
graph.add_edge(START, 'llm_qa')
graph.add_edge('llm_qa', END)
   
#compile the graph
workflow = graph.compile()

#execute the workflow
initial_state={ 'question': "What is LangGraph?" }
final_state=workflow.invoke(initial_state)
print(final_state)