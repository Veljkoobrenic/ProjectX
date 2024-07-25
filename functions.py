from PyPDF2 import PdfReader
import instructor
from openai import OpenAI
from prompt_templates import SYSTEM_PROMPT_Classification
from llm_chains import TicketClassification

client = instructor.patch(OpenAI())

def get_pdf_text(pdfs):
    """Extract text from PDF documents.

    Args:
        pdf_docs (list): List of PDF documents.

    Returns:
        str: Concatenated text extracted from the PDFs.
    """
    # extract the text
    docs = ''
    for pdf in pdfs:
        loader = PdfReader(pdf)
        for page in loader.pages:
            docs += page.extract_text()
    return docs

def classify_ticket(ticket_text: str) -> TicketClassification:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=TicketClassification,
        temperature=0,
        max_retries=3,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT_Classification,
            },
            {"role": "user", "content": ticket_text}
        ]
    )
    return response
