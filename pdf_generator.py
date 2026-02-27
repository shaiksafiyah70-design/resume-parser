from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

print("PDF Generator Started...")


def generate_pdf(text, filename="final_resume.pdf"):

    c = canvas.Canvas(filename, pagesize=letter)

    width, height = letter

    y = height - 40

    for line in text.split("\n"):

        c.drawString(40, y, line)

        y -= 15

        if y < 40:
            c.showPage()
            y = height - 40

    c.save()

    print("PDF Created:", filename)


# Test Run
if __name__ == "__main__":

    sample_text = """
    SAFIYAH

    Skills:
    Python
    Machine Learning
    Pandas

    Projects:
    Resume Parser AI
    Job Matcher AI
    """

    generate_pdf(sample_text)