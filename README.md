# AI CV Screening Tool

This is an AI-powered web application that:
- Uploads and reads CVs (PDF)
- Uses OpenAI to generate CV summaries
- Compares CVs against a job description
- Provides a score, strengths, and weaknesses

## Tech Stack
- Python
- Streamlit
- OpenAI API
- pdfplumber

## How to Run

### 1. Install dependencies


pip install -r requirements.txt


### 2. Set up environment variables

Create a `.env` file in the project root:


OPENAI_API_KEY=your_api_key_here


### 3. Run the application


python -m streamlit run app.py


### 4. Open in browser


http://localhost:8501


---

## Features

- AI-powered CV summarisation  
- CV vs Job Description scoring  
- Recruiter-style insights  
- Simple web interface using Streamlit  
