import streamlit as st
#import chatbot object from backend file
from AIChatbot_Backend import chatbot #Call Direct to Object
from langchain_core.messages import HumanMessage

#Thread configuration for checkpointer
CONFIG = {'configurable': {'thread_id':'tread-1'}}
#st.session_state to store chat history which does not get deleted on every interaction
if 'messages_history' not in st.session_state:
    st.session_state['messages_history'] = []
for message in st.session_state['messages_history'] :
    with st.chat_message(message["role"]):
        st.text(message["content"])
#User intput field
user_input= st.chat_input("Your message")
#User intput action
if user_input:
    st.session_state['messages_history'].append({"role":"user","content":user_input})
    with st.chat_message('user'):
        st.text(user_input)
    response = chatbot.invoke({'message':[HumanMessage(content=user_input)]}, config=CONFIG)
    ai_message = response['messages'][-1].content
    st.session_state['messages_history'].append({"role":"assistant","content":ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)