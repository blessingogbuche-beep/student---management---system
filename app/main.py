from app import app
from flask import render_template, request, redirect, url_for
from app.database import create_database
import sqlite3


create_database()

@app.route("/", methods=["GET", "POST"])
def register_student():

    if request.method == "POST":
        name = request.form["name"]
        age = int(request.form["age"])
        student_class = request.form["class"]
        gender = request.form["gender"]
        date_of_birth = request.form["date_of_birth"]
        parent_guardian = request.form["parent_guardian"]
        parent_email = request.form["parent_email"]
        phone = request.form["phone"]

        if age < 9:
            return "Student is too young for secondary school."

        elif age > 20:
            return "Student is above the allowed age."

        else:
            message = "Student registration accepted."

        connection = sqlite3.connect("students.db")

        connection.execute(
            """
            INSERT INTO students (
                name,
                age,
                student_class,
                gender,
                date_of_birth,
                parent_guardian,
                parent_email,
                phone
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                age,
                student_class,
                gender,
                date_of_birth,
                parent_guardian,
                parent_email,
                phone
            )
        )

        connection.commit()
        connection.close()

        return render_template("index.html",success=True)
    return render_template("index.html",success=False)


