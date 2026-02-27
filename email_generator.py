from groq import Groq
import os

def generate_email(parsed_data, job_description):

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
    Write a professional job application email.

    Candidate Name:
    {parsed_data.get('name')}

    Job Description:
    {job_description}

    Include:
    - Subject line
    - Professional email body
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content