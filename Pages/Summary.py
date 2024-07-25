import streamlit as st 
import os
from dotenv import load_dotenv
from Main_page import *
from langchain_openai import ChatOpenAI
import openai
from langchain.memory import ConversationBufferWindowMemory
from llm_chains import *
from langchain.memory import StreamlitChatMessageHistory
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from llm_chains import summery_chain
st.header('Summarize your pdf file', divider='red')


def main():
    if "pdf_text" in st.session_state:
        pdf_text = st.session_state["pdf_text"]
    
        # Define LLM chain
        llm_chain = summery_chain()
        llm_response = llm_chain.run(pdf_text)
        st.chat_message("ai").write(llm_response)
    else:
        st.write("No PDF text found. Please upload a PDF on the previous page.")

if __name__ == '__main__':
    main()