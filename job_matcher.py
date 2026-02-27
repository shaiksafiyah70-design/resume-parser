import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Job Matcher Loaded...")


def match_job(parsed_data, job_description):

    prompt = f"""

Compare the resume with the job description.

Return the result in EXACT format:

MATCH ANALYSIS REPORT

Job Description Skills:
- skill1
- skill2
- skill3

Resume Skills:
- skill1
- skill2

Matching Skills:
- skill1
- skill2

Missing Skills:
- skill1
- skill2

Match Percentage:
XX %

Resume Data:
{parsed_data}

Job Description:
{job_description}

"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content