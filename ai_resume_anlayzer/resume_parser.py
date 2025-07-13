import pdfplumber
from docx import Document

def extract_text_from_pdf(file):
    try:
        with pdfplumber.open(file) as pdf:
            text = "\n".join([page.extract_text() or '' for page in pdf.pages])
        return text.strip() or "[ERROR] No text extracted from PDF."
    except Exception as e:
        return f"[ERROR] Failed to read PDF: {e}"

def extract_text_from_docx(file):
    try:
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        return f"[ERROR] Failed to read DOCX: {e}"

