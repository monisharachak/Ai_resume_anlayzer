import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from job_matcher import match_resume_with_job
from feedback_generator import generate_resume_feedback

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("📄 AI Resume Analyzer with Ollama")

uploaded_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_input = st.text_area("Paste the Job Description")

if st.button("Analyze Resume"):
    if uploaded_file and jd_input.strip():
        file_type = uploaded_file.name.split('.')[-1].lower()
        if file_type == "pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif file_type == "docx":
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file type.")
            st.stop()

        with st.spinner("Analyzing..."):
            match_score, missing_keywords = match_resume_with_job(resume_text, jd_input)
            feedback = generate_resume_feedback(resume_text, jd_input)

        st.subheader("✅ Match Score:")
        st.progress(match_score / 100)
        st.success(f"Your resume matches {match_score:.2f}% of the job description.")

        st.subheader("❌ Missing Keywords:")
        st.write(missing_keywords if missing_keywords else "All important keywords are covered.")

        st.subheader("🤖 AI Feedback:")
        st.write(feedback)
    else:
        st.warning("Please upload a resume and paste a job description.")
