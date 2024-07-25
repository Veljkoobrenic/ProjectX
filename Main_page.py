import streamlit as st 
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from functions import get_pdf_text

def main():
    st.header('Welcome to the allpdf application', divider='red')
    st.header('Pleas upload your pdf files')

    load_dotenv()
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    langchain_api_key = os.environ["LANGCHAIN_API_KEY"] 
    pdf = st.file_uploader("Upload PDF",accept_multiple_files=True, type ='pdf') 
    if pdf is not None: 
        if st.button("Upload"):
            with st.spinner("Processing"):
                pdf_text = get_pdf_text(pdf)
                st.write(pdf_text)
                st.session_state['pdf_text'] = pdf_text
    else:
        st.write('Please upload Pdf files')

if __name__ == '__main__':
    main()