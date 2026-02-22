from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
#store chart history to RAM import memorysaver 
from langgraph.checkpoint.memory import Memorysaver     
from langgraph.graph.message import add_messages # Reducer
from dotenv import load_dotenv

load_dotenv()

#create schema
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

#create LLM object
llm = ChatOpenAI()

#define action for Chat_node function
def chat_node(state: ChatState):
    # take user query from state
    messages = state['messages']
    # send to llm
    response = llm.invoke(messages)
    # response store state
    return {'messages': [response]}

#Create memory object
checkpointer=Memorysaver()

graph = StateGraph(ChatState)
# add nodes
graph.add_node('chat_node', chat_node)

# add edges
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

#intigrate memory reference while compile
chatbot = graph.compile(checkpointer=checkpointer)

# test the LLM with human message
initial_state = {
    'messages': [HumanMessage(content='What is the capital of india')]
}
chatbot.invoke(initial_state)['messages'][-1].content

#test the LLM with continue feeding human message
#Create Thread ID to monitor or track for Agent ID if multiple users are chatting
 
thread_id='1'
while True:
    user_message = input("type your message: ")
    if user_message.lower() in ['exit', 'quit','bye']:
        break
    config = {'configurable': {'thread_id': thread_id}}
    response = chatbot.invoke({
        'messages': [HumanMessage(content=user_message)]}, config=config)
    
print("AI Bot:", response['messages'][-1].content)
#Print the History of Chat
print(chatbot.get_state(config=config))
