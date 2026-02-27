from flask import Flask, render_template, request
from pdf_reader import read_pdf
from resume_parser import parse_resume_with_ai
from job_matcher import match_job
from resume_tailor import tailor_resume
from pdf_generator import generate_pdf

from cover_letter_generator import generate_cover_letter
from email_generator import generate_email
from skills_gap import skills_gap_analysis

app = Flask(__name__)
def skill_gap(parsed_data, job_description):

    resume_skills = parsed_data.get("skills", [])

    job_skills = job_description.lower().split()

    missing_skills = []

    for skill in job_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    return missing_skills

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        file = request.files["resume"]
        file.save("uploaded_resume.pdf")

        job_description = request.form["job_description"]

        resume_text = read_pdf("uploaded_resume.pdf")

        parsed_data = parse_resume_with_ai(resume_text)

        match = match_job(parsed_data, job_description)

        improved_resume = tailor_resume(parsed_data, job_description)

        generate_pdf(improved_resume)

        cover_letter = generate_cover_letter(parsed_data, job_description)

        email = generate_email(parsed_data, job_description)

        gap = skills_gap_analysis(parsed_data, job_description)


        return render_template(
            "result.html",
            match=match,
            cover_letter=cover_letter,
            email=email,
            gap=gap
        )


    return render_template("index.html")


app.run(debug=True)