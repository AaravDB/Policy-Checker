import requests
import fitz  # PyMuPDF

def extract_text_from_pdf_url(url):
    response = requests.get(url)
    with open("temp.pdf", "wb") as f:
        f.write(response.content)
    doc = fitz.open("temp.pdf")
    text = "\n".join([page.get_text() for page in doc])
    return text
