# utils.py
def extract_tech_stack(user_input):
    keywords = ["python", "java", "c++", "react", "django", "flask", "node", "sql", "mongodb", "git", "docker"]
    return [kw for kw in keywords if kw in user_input.lower()]

def generate_questions(tech_stack):
    question_bank = {
        "python": [
            "Explain the difference between a list and a tuple in Python.",
            "What are Python decorators and how do they work?"
        ],
        "django": [
            "What is the role of middleware in Django?",
            "How does Django handle database migrations?"
        ],
        "react": [
            "What is a React hook? Explain useEffect with an example.",
            "How is state management handled in React?"
        ],
        "sql": [
            "What is the difference between WHERE and HAVING in SQL?",
            "Explain normalization and its types."
        ],
        # Add more as needed
    }

    questions = []
    for tech in tech_stack:
        if tech in question_bank:
            questions += question_bank[tech][:2]  # Pick 2 from each tech
    return questions
