import ollama

def generate_resume_feedback(resume_text, job_desc):
    try:
        model_name = 'llama3.2:1b'  # Must match `ollama list`

        messages = [
            {
                "role": "system",
                "content": "You are an AI resume reviewer. Provide professional and helpful feedback."
            },
            {
                "role": "user",
                "content": f"""Resume:
{resume_text}

Job Description:
{job_desc}

Please review this resume for the above job description and suggest improvements, missing skills, and feedback."""
            }
        ]

        response = ollama.chat(
            model=model_name,
            messages=messages
        )

        return response['message']['content']
    except Exception as e:
        return f"[ERROR] AI feedback failed: {e}"
