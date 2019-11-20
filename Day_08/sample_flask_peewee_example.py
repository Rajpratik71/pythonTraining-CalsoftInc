"""
Module to demonstrate peewee usage in a flask application.
"""
import json

from flask import Flask
from peewee import MySQLDatabase, Model, TextField, IntegerField, CharField, AutoField

mysql_db = MySQLDatabase("Students", user="root", password="root")

app = Flask(__name__)


class BaseModel(Model):
    class Meta:
        database = mysql_db


class Students_pewee(BaseModel):
    """
    Student model
    """

    student_id = AutoField()
    first_name = TextField()
    last_name = TextField()
    age = IntegerField()
    gender = CharField()


@app.route("/list_students", methods=["GET"])
def list_students():
    """
    Controller to accept and serve list students rest end point

    Returns:
        List: students information
    """
    students = Students_pewee.select()
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
    with mysql_db.atomic():
        Students_pewee.create(first_name="New", last_name="Student", age=15, gender="F")
    return json.dumps({"result": "success"})


def create_tables():
    """
    Create tables if not exists
    """
    with mysql_db:
        mysql_db.create_tables([Students_pewee])
        Students_pewee.truncate_table()


if __name__ == "__main__":
    create_tables()
    app.run(port=8082, debug=True)
