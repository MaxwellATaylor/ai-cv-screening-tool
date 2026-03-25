import streamlit as st
import pdfplumber
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI CV Screening Tool")

# Input
job_description = st.text_area("Paste Job Description")
uploaded_file = st.file_uploader("Upload a CV (PDF)")

# Extract text
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# AI: Analyse CV vs Job
def analyse_cv(cv_text, job_description):
    prompt = f"""
    You are a recruiter.

    Compare the CV with the job description.

    Give:
    - A score out of 100
    - Short reasoning
    - Strengths
    - Weaknesses

    CV:
    {cv_text}

    Job Description:
    {job_description}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# AI: Simple summary
def summarise(cv_text):
    prompt = f"""
    Summarise this CV into:
    - Short summary
    - Key skills
    - Experience

    CV:
    {cv_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# MAIN LOGIC
if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("AI Summary")
    st.write(summarise(text))

    if job_description:
        st.subheader("AI CV Score vs Job Description")
        st.write(analyse_cv(text, job_description))