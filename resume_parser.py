import os
import json
import re
from groq import Groq
from dotenv import load_dotenv
import PyPDF2

print("Resume Parser Loaded...")

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------
# READ PDF
# ---------------------------
def read_pdf(file_path):

    print("Reading PDF...")

    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text


# ---------------------------
# AI RESUME PARSER
# ---------------------------
def parse_resume_with_ai(resume_text):

    print("Sending to AI...")

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role": "system",
                "content":
                """
Extract resume information in STRICT JSON format.

Return ONLY JSON like this:

{
 "Name":"",
 "Email":"",
 "Phone":"",
 "Skills":[],
 "Education":"",
 "Experience":""
}
"""
            },

            {
                "role": "user",
                "content": resume_text
            }

        ]

    )

    ai_output = completion.choices[0].message.content

    print("AI Raw Output:")
    print(ai_output)


    # ---------------------------
    # Extract JSON safely
    # ---------------------------
    try:

        json_text = re.search(r'\{.*\}', ai_output, re.DOTALL).group()

        parsed_data = json.loads(json_text)

        print("\n✅ Parsed JSON Ready\n")

        return parsed_data

    except:

        print("❌ JSON Parsing Failed")

        return {
            "Name":"Unknown",
            "Email":"Unknown",
            "Phone":"Unknown",
            "Skills":[],
            "Education":"Unknown",
            "Experience":"Unknown"
        }


# ---------------------------
# TEST RUN (Optional)
# ---------------------------
if __name__ == "__main__":

    resume_text = read_pdf("sample_resume.pdf")

    result = parse_resume_with_ai(resume_text)

    print("\n✅ Parsed Resume:\n")

    print(result)