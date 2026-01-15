print("🔥 THIS APP.PY IS RUNNING 🔥")

from flask import Flask, render_template, request, jsonify
from ai_engine import (
    analyze_student,
    chat_with_ai,
    generate_interview_question,
    evaluate_interview,
    recommend_training_path
)

app = Flask(__name__)

@app.route("/test")
def test():
    return "Flask is working perfectly"


# HOME
@app.route("/")
def index():
    return render_template("index.html")


# STUDENT REGISTRATION
@app.route("/student", methods=["GET", "POST"])
def student():
    if request.method == "POST":
        name = request.form.get("name")
        year = request.form.get("year")
        skills = request.form.get("skills")
        interest = request.form.get("interest")

        try:
            cgpa = float(request.form.get("cgpa", 0))
        except:
            cgpa = 0.0

        ai_result = analyze_student(year, skills, interest, cgpa)

        if year in ["1st", "2nd", "3rd"]:
            return render_template(
                "training.html",
                name=name,
                year=year,
                interest=interest,
                ai_result=ai_result
            )
        else:
            return render_template(
                "placement.html",
                name=name,
                year=year,
                interest=interest,
                ai_result=ai_result
            )

    return render_template("student.html")


# AI CHAT
@app.route("/ai-chat", methods=["POST"])
def ai_chat():
    msg = request.form.get("message")
    return jsonify({"reply": chat_with_ai(msg)})


# MOCK INTERVIEW
@app.route("/mock-interview")
def mock_interview():
    q = generate_interview_question("technical")
    return render_template("mock_interview.html", question=q)


@app.route("/submit-interview", methods=["POST"])
def submit_interview():
    answer = request.form.get("answer")
    score, feedback = evaluate_interview(answer)
    return render_template(
        "interview_result.html",
        score=score,
        feedback=feedback
    )


# INDUSTRY TRAINING PATH
@app.route("/training-path/<interest>")
def training_path(interest):
    modules = recommend_training_path(interest)
    return render_template(
        "training_path.html",
        interest=interest,
        modules=modules
    )


if __name__ == "__main__":
    app.run(debug=True)
