import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_cover_letter(parsed_data, job_description):

    name = parsed_data.get("Name","Candidate")
    skills = ", ".join(parsed_data.get("Skills",[]))
    education = parsed_data.get("Education","")
    experience = parsed_data.get("Experience","")

    prompt = f"""
Write a professional job application cover letter.

Candidate Name: {name}
Education: {education}
Experience: {experience}
Skills: {skills}

Job Description:
{job_description}

Rules:
- Do NOT use placeholders
- Use real candidate name
- Make it professional
- 150-250 words
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {"role":"user","content":prompt}
        ]

    )

    return response.choices[0].message.content