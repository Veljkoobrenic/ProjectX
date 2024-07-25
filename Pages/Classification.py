import streamlit as st 
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import instructor
from openai import OpenAI
from prompt_templates import SYSTEM_PROMPT_Classification
from llm_chains import TicketClassification
from functions import *
from llm_chains import *
import pandas as pd
import json

def main():
    st.header('Text classification', divider='red')
    load_dotenv()
    chat_container = st.container()
    user_input = st.chat_input("Type your message here", key="user_input", on_submit= set_send_imput )

    if "send_input" not in st.session_state:
            st.session_state.send_input = False
            st.session_state.user_input = ''
    
    if st.session_state.send_input:
        if st.session_state.user_input != "":

            with chat_container:
                st.chat_message("user").write(st.session_state.user_input)
                ticket = classify_ticket(st.session_state.user_input)
                llm_response = json.loads(ticket.model_dump_json(indent=2))
                df = pd.DataFrame(llm_response)
                st.write(df)
                st.write(llm_response)
                #st.chat_message("ai").write(llm_response)


if __name__ == '__main__':
    main()