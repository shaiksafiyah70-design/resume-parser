import os
from groq import Groq
from dotenv import load_dotenv

print("Resume Tailor Started...")

# Load API Key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def tailor_resume(resume_text, job_description):

    prompt = f"""
    Improve the following resume based on the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Create an improved professional resume.
    Keep it realistic and structured.
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return completion.choices[0].message.content


# Test Run
if __name__ == "__main__":

    resume_text = open("resume.txt").read()

    job_description = """
    We are hiring a Python Developer.

    Required Skills:
    - Python
    - Machine Learning
    - Pandas
    - API Development
    - Git
    """

    result = tailor_resume(resume_text, job_description)

    print("\nImproved Resume:\n")
    print(result)