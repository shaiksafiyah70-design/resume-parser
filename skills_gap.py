import os
from groq import Groq
from dotenv import load_dotenv

print("Skills Gap Module Loaded...")

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def skills_gap_analysis(parsed_data, job_description):

    print("Skills Gap Analysis Started...")

    prompt = f"""
Analyze the difference between Resume Skills and Job Description.

Resume Skills:
{parsed_data.get('skills')}

Job Description:
{job_description}

Return clearly in this format:

Missing Skills:
- skill1
- skill2

Recommended Courses:
- course1
- course2

Improvement Suggestions:
- suggestion1
- suggestion2
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content