"""
Module to demonstrate connection and communication to  mysql database in python.
"""

import mysql.connector
from mysql.connector import Error


# =========Database connection example========================
def connect():
    """
    Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost", database="Students", user="root", password="root"
        )
        if conn.is_connected():
            print("Connected to MySQL database")

    except Error as ex:
        print(ex)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    connect()


# =========Demonstrate mysql DML operations in python========================


# def connect():
#     """
#     Connect to MySQL database
#     """
#     conn = None
#     try:
#         conn = mysql.connector.connect(
#             host="localhost", database="Students", user="root", password="root"
#         )
#         if conn.is_connected():
#             print("Connected to MySQL database")
#
#         cursor = conn.cursor(prepared=True)
#
#         insert_single = (
#             "INSERT INTO students(first_name, last_name, age, gender)  VALUES(%s,%s, %s, %s)"
#         )
#         student = ("John", "White", 16, "M")
#
#         insert_many = (
#             "INSERT INTO students(first_name, last_name, age, gender) VALUES(%s,%s, %s, %s)"
#         )
#         students = [("Alex", "Brown", 15, "M"), ("Mery", "d'souza", 16, "F")]
#
#         cursor.execute(insert_single, student)
#         cursor.executemany(insert_many, students)
#
#         conn.commit()
#
#         cursor.execute("SELECT * FROM students")
#
#         row = cursor.fetchone()
#
#         while row is not None:
#             print(row)
#             row = cursor.fetchone()
#
#     except Error as ex:
#         print(ex)
#
#     finally:
#         if conn is not None and conn.is_connected():
#             cursor.close()
#             conn.close()
#
#
# if __name__ == "__main__":
#     connect()
