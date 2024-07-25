from Main_page import *
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from prompt_templates import *
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from prompt_templates import *
from pydantic import BaseModel, Field
from openai import OpenAI
from enum import Enum
from typing import List

def set_send_imput():
    st.session_state.send_input = True

def create_chat_history(chat_history):
    return ConversationBufferWindowMemory(memory_key="history", chat_memory=chat_history, k=3)

def create_prompt_from_template(template):
    return PromptTemplate.from_template(template)

def create_llm_chain(llm, chat_prompt):
    return LLMChain(llm=llm, prompt=chat_prompt)

def load_normal_chain(chat_history):
    return chatChain(chat_history)

def summery_chain():
    return SummeryChain()

#chat with your data 
class chatChain:

    def __init__(self,chat_history):
        llm = ChatOpenAI()
        self.memory = create_chat_history(chat_history)
        chat_prompt = create_prompt_from_template(prompt_template)
        self.llm_chain = create_llm_chain(llm, chat_prompt)

    def run(self, user_input, chat_history, pdf_text):
        return self.llm_chain.invoke(input={ "pdf_text": pdf_text, "user_input" : user_input, "history" : chat_history} ,stop=["Human:"])["text"]

#summery 
class SummeryChain:
    def __init__(self):
        llm = ChatOpenAI()
        chat_prompt = create_prompt_from_template(prompt_template_summary)
        self.llm_chain = create_llm_chain(llm, chat_prompt)

    def run(self, pdf_text):
        return self.llm_chain.invoke(input={ "pdf_text": pdf_text})["text"]


#classification 
class TicketCategory(str, Enum):
    ORDER_ISSUE = "order_issue"
    ACCOUNT_ACCESS = "account_access"
    PRODUCT_INQUIRY = "product_inquiry"
    TECHNICAL_SUPPORT = "technical_support"
    BILLING = "billing"
    OTHER = "other"

class CustomerSentiment(str, Enum):
    ANGRY = "angry"
    FRUSTRATED = "frustrated"
    NEUTRAL = "neutral"
    SATISFIED = "satisfied"

class TicketUrgency(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class TicketClassification(BaseModel):
    category: TicketCategory
    urgency: TicketUrgency
    sentiment: CustomerSentiment
    confidence: float = Field(ge=0, le=1, description="Confidence score for the classification")
    key_information: List[str] = Field(description="List of key points extracted from the ticket")
    suggested_action: str = Field(description="Brief suggestion for handling the ticket")
    
    
