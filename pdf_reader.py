import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):

    text = ""

    pdf = fitz.open(pdf_path)

    for page in pdf:
        text += page.get_text()

    return text
import PyPDF2

print("PDF Reader Loaded")


def read_pdf(file_path):

    print("Reading PDF...")

    text = ""

    with open(file_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            text += page.extract_text()

    return text