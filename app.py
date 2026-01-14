from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# ✅ YAHI PE ADD KARNA HAI (MySQL CONFIG)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'SHRAVANI@2006'  # Mac me password hota hai
app.config['MYSQL_DB'] = 'ai_training'

mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/student", methods=["GET", "POST"])
def student():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        college = request.form['college']
        year = request.form['year']
        branch = request.form['branch']
        skills = request.form['skills']
        cgpa = request.form['cgpa']

        # 🔹 INSERT into MySQL
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO students
            (name, email, mobile, college, year, branch, skills, cgpa)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (name, email, mobile, college, year, branch, skills, cgpa))

        mysql.connection.commit()
        cur.close()

        # 🔹 Redirect based on year
        if year in ["1st", "2nd"]:
            return redirect(url_for("skills_dashboard"))
        else:
            return redirect(url_for("placement_dashboard"))

    return render_template("student.html")

@app.route("/skills-dashboard")
def skills_dashboard():
    return render_template("skills.html")

@app.route("/placement-dashboard")
def placement_dashboard():
    return render_template("placement.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
