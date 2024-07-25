import streamlit as st 
import os
from dotenv import load_dotenv
from Main_page import *
from llm_chains import *
from langchain.memory import StreamlitChatMessageHistory



def main():
    st.write(st.session_state)
    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_input = ''

    load_dotenv()
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    st.header('Chat with your data', divider='red')
    chat_container = st.container()
    chat_history = StreamlitChatMessageHistory(key="history")
    llm_chain = load_normal_chain(chat_history)
    user_input = st.chat_input("Type your message here", key="user_input", on_submit= set_send_imput )
    
    if "pdf_text" in st.session_state:
        st.session_state.pdf_text = st.session_state["pdf_text"]
    else:
        st.write("No PDF text found. Please upload a PDF on the previous page.")
    
    if st.session_state.send_input:
        if st.session_state.user_input != "":

            with chat_container:
                st.chat_message("user").write(st.session_state.user_input)
                llm_response = llm_chain.run(st.session_state.user_input, st.session_state.chat_history, st.session_state.pdf_text)
                st.chat_message("ai").write(llm_response)

    if chat_history.messages != []:
        with chat_container:
            st.write("Chat History:")
            for message in chat_history.messages:
                st.chat_message(message.type).write(message.content)

    
    
    
if __name__ == '__main__':
    main()