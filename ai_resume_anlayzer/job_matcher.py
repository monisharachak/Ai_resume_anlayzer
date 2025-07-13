from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', text).lower()

def match_resume_with_job(resume_text, job_desc):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(job_desc)
    vectorizer = CountVectorizer().fit([resume_clean, jd_clean])
    vectors = vectorizer.transform([resume_clean, jd_clean])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0] * 100
    resume_words = set(resume_clean.split())
    jd_words = set(jd_clean.split())
    missing = list(jd_words - resume_words)
    return similarity, missing
