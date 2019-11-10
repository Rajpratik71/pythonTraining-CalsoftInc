"""
Module to demonstrate SQLAlchemy usage in a flask application.
"""
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Students"


db = SQLAlchemy(app)


class Students(db.Model):
    """
        Student model
    """
    id = db.Column("student_id", db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender


@app.route("/list_students", methods=["GET"])
def list_students():
    """
    Controller to accept and serve list students rest end point

    Returns:
        List: students information
    """
    students = Students.query.all()
    student_list = []
    for student in students:
        student_list.append(
            {
                "first_name": student.first_name,
                "last_name": student.last_name,
                "age": student.age,
                "gender": student.gender,
            }
        )
    return json.dumps(student_list)


@app.route("/add_new_student", methods=["GET"])
def add_student():
    """
    Controller function to accept request to add new student rest end point
    Returns:
        Dict: operation result status
    """
    student = Students("New", "Student", 15, "F")
    db.session.add(student)
    db.session.commit()
    return json.dumps({"result": "success"})


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
