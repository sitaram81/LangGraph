from langgraph.graph import StateGraph,START, END
from typing import TypedDict

class BMIState(TypedDict):
    height: float  # in meters
    weight: float  # in kilograms
    bmi: float     # Body Mass Index

def calculate_bmi(state: BMIState) -> BMIState:
    bmi = state['weight'] / (state['height'] ** 2)
    state['bmi'] = bmi
    return state

#define your graph
bmi_graph = StateGraph(BMIState)

#add nodes to your graph
bmi_graph.add_node("calculate_bmi", calculate_bmi)

#add edges to your graph
bmi_graph.add_edge(START, "calculate_bmi")
bmi_graph.add_edge("calculate_bmi", END)

#compile your graph
workflow=bmi_graph.compile()

#Execute the workflow
initial_state={ 'weight': 80, 'height': 1.73 }
final_state=workflow.invoke(initial_state)
print(final_state)

#answer
#{'height': 1.73, 'weight': 80, 'bmi': 26.729927495071667}