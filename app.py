import os
import re
from io import BytesIO

import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Analyze a resume against a job description and identify skills, missing keywords, and improvement suggestions.")

def extract_pdf_text(file_bytes):
    reader = PdfReader(BytesIO(file_bytes))
    return "\n".join(page.extract_text() or "" for page in reader.pages).strip()

def basic_analyze(resume_text, job_description):
    resume_words = set(re.findall(r"[A-Za-z][A-Za-z+#.-]{1,}", resume_text.lower()))
    jd_words = set(re.findall(r"[A-Za-z][A-Za-z+#.-]{1,}", job_description.lower()))

    stop = {
        "the","and","for","with","that","this","are","you","your","from","have",
        "will","our","their","into","using","about","job","role","years","work"
    }
    keywords = sorted((jd_words - stop), key=len, reverse=True)
    matched = [w for w in keywords if w in resume_words]
    missing = [w for w in keywords if w not in resume_words][:20]

    return matched[:20], missing

uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the Job Description", height=220)

if st.button("Analyze Resume", type="primary"):
    if not uploaded:
        st.error("Please upload a PDF resume.")
    elif not job_description.strip():
        st.error("Please paste a job description.")
    else:
        resume_text = extract_pdf_text(uploaded.read())

        if not resume_text:
            st.error("Could not extract text from this PDF.")
        else:
            matched, missing = basic_analyze(resume_text, job_description)

            st.subheader("📊 Analysis")
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### ✅ Matching Keywords")
                st.write(", ".join(matched) if matched else "No strong keyword matches found.")

            with col2:
                st.markdown("### ⚠️ Potential Missing Keywords")
                st.write(", ".join(missing) if missing else "No obvious missing keywords found.")

            st.markdown("### 💡 Improvement Suggestions")
            suggestions = [
                "Add measurable achievements where possible (for example: improved accuracy by X% or reduced processing time by Y%).",
                "Use the exact technical terms from the job description when they truthfully match your experience.",
                "Keep project descriptions focused on your contribution, technologies used, and outcome.",
                "Put the most relevant skills and projects near the top of the resume.",
            ]
            for item in suggestions:
                st.write("• " + item)

            st.success("Basic resume analysis completed.")

            # Optional OpenAI integration
            if os.getenv("OPENAI_API_KEY"):
                st.info("OPENAI_API_KEY detected. You can extend this app with an LLM-based analysis using the OpenAI SDK.")
