from pdf_reader import read_pdf
from resume_parser import parse_resume_with_ai
from job_matcher import match_job

def batch_process(resumes, job_description):

    results = []

    for resume in resumes:

        text = read_pdf(resume)

        parsed = parse_resume_with_ai(text)

        score = match_job(parsed, job_description)

        results.append(score)

    return results