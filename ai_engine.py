from industry_data import INDUSTRY_ROLES


def analyze_student(year, skills, interest, cgpa):
    roadmap = []

    if year in ["1st", "2nd"]:
        roadmap = ["Programming Basics", "Logic Building", "Communication"]
    elif year == "3rd":
        roadmap = ["Projects", "Advanced Skills", "Mock Interviews"]
    else:
        roadmap = ["Placement Prep", "Resume", "Company Practice"]

    return {
        "skills": skills,
        "interest": interest,
        "cgpa": cgpa,
        "roadmap": roadmap
    }


def chat_with_ai(message):
    if not message:
        return "Please ask something."

    if "interview" in message.lower():
        return "You should practice mock interviews regularly."

    if "skill" in message.lower():
        return "Focus on one strong domain and build projects."

    return "I will guide you step by step based on your profile."


def generate_interview_question(domain):
    questions = {
        "technical": "Explain OOPS concepts in Python.",
        "hr": "Tell me about yourself.",
        "aptitude": "What is the next number: 2, 4, 8, 16?"
    }
    return questions.get(domain, "Explain your skills.")


def evaluate_interview(answer):
    score = min(len(answer.split()) // 5, 10)
    feedback = "Good effort. Improve clarity and structure."
    return score, feedback


def recommend_training_path(interest):
    return INDUSTRY_ROLES.get(
        interest,
        ["Programming Fundamentals", "Projects", "Interview Prep"]
    )
