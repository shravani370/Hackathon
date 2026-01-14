from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# HOME
@app.route("/")
def index():
    return render_template("index.html")

# STUDENT REGISTRATION
@app.route("/student", methods=["GET", "POST"])
def student():
    if request.method == "POST":
        year = request.form["year"]

        # year ke basis pe redirect
        if year in ["1st", "2nd"]:
            return redirect(url_for("training"))
        else:
            return redirect(url_for("placement"))

    return render_template("student.html")

# TRAINING PAGE (1st & 2nd year)
@app.route("/training")
def training():
    return render_template("training.html")

# PLACEMENT PAGE (3rd & 4th year)
@app.route("/placement")
def placement():
    return render_template("placement.html")

if __name__ == "__main__":
    app.run(debug=True)
