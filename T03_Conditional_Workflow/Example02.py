from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

class SentimentSchema(BaseModel):
    sentiment: Literal["positive","negative"] = Field(description='Sentiment of the review')

class DiagnosisSchema(BaseModel):
    issue_type: Literal["UX", "Performance", "Bug", "Support", "Other"] = Field(description='The category of issue mentioned in the review')
    tone: Literal["angry", "frustrated", "disappointed", "calm"] = Field(description='The emotional tone expressed by the user')
    urgency: Literal["low", "medium", "high"] = Field(description='How urgent or critical the issue appears to be')

class ReviewState(TypedDict):
    review: str
    sentiment: Literal["positive","negative"]
    diagnosis:dict
    response:str

#Conditional check
def checkSentiment(state:ReviewState) -> Literal['positive_response','run_diagnosis']:
    if state['sentiment']=="positive":
        return 'positive_response'
    else:
        return 'run_diagnosis'
    
def find_sentiment(state:ReviewState):
    prompt = f'for the following review findout the sentiment \n {state["review"]}'
    sentiment=Structured_model.invoke(prompt).sentiment
    return {'sentiment': sentiment}

def positive_response(state:ReviewState):
    prompt = f"""Write a warm thank-you message in response to this review:
    \n\n\"{state['review']}\"\n
    Also, kidnly ask the user to leave feedback on our website."""
    response=model.invoke(prompt).content
    return {'response': response  }

def run_diagnosis(state:DiagnosisSchema):
    prompt = f"""Diagnose this negative review:\n\n{state['review']}\n"
    "Return issue_type, tone, and urgency."""
    response = Structured_model2.invoke(prompt)
    return {'diagnosis': response.model_dump()}

def negative_response(state:DiagnosisSchema):
    diagnosis = state['diagnosis']
    prompt = f"""You are a support assistant.
    The user had a '{diagnosis['issue_type']}' issue, sounded '{diagnosis['tone']}', and marked urgency as '{diagnosis['urgency']}'.
    Write an empathetic, helpful resolution message.
    """
    response = model.invoke(prompt).content
    return {'response': response}

model = ChatOpenAI(model='gpt-4o-mini')
Structured_model= model.with_structured_output(SentimentSchema)
Structured_model2= model.with_structured_output(DiagnosisSchema)

#Test LLM output by providing sample prompt
prompt='What is the sentiment of the following review - The softare too bad'
Structured_model.invoke(prompt).sentiment

graph = StateGraph(ReviewState)

graph.add_node('find_sentiment',find_sentiment)
graph.add_node('positive_response',positive_response)
graph.add_node('run_diagnosis',run_diagnosis)
graph.add_node('negative_response',negative_response)

graph.add_edge(START, 'find_sentiment')

graph.add_conditional_edges('find_sentiment',checkSentiment)

graph.add_edge('positive_response',END)
graph.add_edge('run_diagnosis','negative_response')
graph.add_edge('negative_response',END)

workflow=graph.compile()
initial_state={
    'review': "I’ve been trying to log in for over an hour now, and the app keeps freezing on the authentication screen. I even tried reinstalling it, but no luck. This kind of bug is unacceptable, especially when it affects basic functionality."
}

print(workflow.invoke(initial_state))
