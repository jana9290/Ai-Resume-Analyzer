# AI Resume Analyzer

An AI-powered resume analysis project built with Python and Streamlit.

## Features

- Upload a resume in PDF format
- Extract resume text
- Compare resume content with a job description
- Identify matching keywords
- Identify potential missing keywords
- Provide resume improvement suggestions
- Optional environment setup for an OpenAI API integration

## Tech Stack

- Python
- Streamlit
- PyPDF
- OpenAI API (optional extension)
- Generative AI / NLP concepts

## Project Structure

```text
AI-Resume-Analyzer/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## How to Run

### 1. Install Python

Use Python 3.10+.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
streamlit run app.py
```

The app will open in your browser.

## Optional OpenAI Setup

Copy `.env.example` to `.env` and add your API key:

```text
OPENAI_API_KEY=your_api_key_here
```

Never upload `.env` or an API key to GitHub.

## Resume Project Description

Developed an AI-powered application to analyze resumes and compare them with job descriptions. The application extracts resume content, identifies matching and missing keywords, and provides suggestions to improve resume relevance for specific job roles.
