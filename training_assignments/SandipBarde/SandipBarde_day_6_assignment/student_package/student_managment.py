"""
class student
"""


class Student:
    """
    Init method for the student
    """

    def __init__(self, roll_number, name, age, percentage):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.percentage = percentage
        self.data = 0

    @staticmethod
    def update_percentage(student_list, roll_number, percentage):
        """ iterates over the student list """
        for stud in student_list:
            if stud.roll_number == roll_number:
                stud.percentage = percentage

    @staticmethod
    def delete_student_record(student_list, roll_number):
        """ iterates over the student list """
        for stud in student_list:
            if stud.roll_number == roll_number:
                student_list.remove(stud)

    def display_student_details(self):
        """ display each student object """
        print("------------- Start ------------------------")
        print(" RollNumber:=", self.roll_number)
        print("\n")
        print(" Name:=", self.name)
        print("\n")
        print(" Age:=", self.age)
        print("\n")
        print(" Percentagee:=", self.percentage)
        print("\n")
        print("-------------- End -----------------------")
