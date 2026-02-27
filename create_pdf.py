from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

doc = SimpleDocTemplate("sample_resume.pdf")

elements = []

text = open("resume.txt").read().split("\n")

for line in text:
    elements.append(Paragraph(line, styles['Normal']))

doc.build(elements)

print("✅ PDF Created Successfully")