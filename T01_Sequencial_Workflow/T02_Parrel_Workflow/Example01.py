"""
Input - runs, balls, fours, sixes
output - strike rate, balls per boundary, boundary percentage, summary

"""

from langgraph.graph import StateGraph,START, END
from typing import TypedDict
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class BatsmanState(TypedDict):
    run:int
    balls:int
    fours:int
    sixes:int
    strike_rate:float
    ballsperboundary:float
    summary:str

def calculate_StrikeRate(state: BatsmanState) -> BatsmanState:
    stikerate = (state['run']/state['balls'])*100
    state['strike_rate']=stikerate  
    # return state will through error as 
	 # simultenously update on same state not possible
	 # return in Dict format to update partially
    return {'strike_rate': stikerate}

def calculate_bpb(state: BatsmanState) -> BatsmanState:
    bps = state['balls']/(state['fours']+state['sixes'])
    state['ballspersboundary']=bps
    # return state will through error as 
	 # simultenously update on same state not possible
	 # return in Dict format to update partially
    return {'ballsperboundary': bps}    

def calculate_boundary_percent(state: BatsmanState) -> BatsmanState:
    boundary_percentage=((state['fours']+state['sixes'])/state['balls'])*100    
    state['boundary_percentage']=boundary_percentage
   # return state will through error as 
	# simultenously update on same state not possible
	# return in Dict format to update partially
    return {'boundary_percentage': boundary_percentage}

def summary(state: BatsmanState) -> BatsmanState:   
    summary = f"""
    Batsman scored {state['run']} \n 
    runs off {state['balls']} balls \n
    with a strike rate of {state['strike_rate']:.2f}."""
    state['summary']=summary
    return state # will work as it is on sequential workflow
    #return {'summary': summary}

graph = StateGraph(BatsmanState)
#add nodes
graph.add_node('calculate_StrikeRate',calculate_StrikeRate)
graph.add_node('calculate_bpb',calculate_bpb)
graph.add_node('calculate_boundary_percent',calculate_boundary_percent)
graph.add_node('summary',summary)

#define edges
#start all the three nodes at a time
graph.add_edge(START,'calculate_StrikeRate')
graph.add_edge(START,'calculate_bpb')
graph.add_edge(START,'calculate_boundary_percent')

#end of all parallel node and connect to summary
graph.add_edge('calculate_StrikeRate','summary')
graph.add_edge('calculate_bpb','summary')
graph.add_edge('calculate_boundary_percent','summary')

#finaly connect summary node to End node
graph.add_edge('summary',END)

workflow = graph.compile()
print(workflow)

#Execute the code by providing intial values

initial_state={ 'run': 150, 'balls': 100, 'fours': 10, 'sixes': 5 }
final_state=workflow.invoke(initial_state)
print(final_state['summary'])
