import time

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
        time.sleep(2)
        for stud in student_list:
            if stud.roll_number == roll_number:
                stud.percentage = percentage

    @staticmethod
    def delete_student_record(student_list, roll_number):
        """ iterates over the student list """
        time.sleep(5)
        for stud in student_list:
            if stud.roll_number == roll_number:
                student_list.remove(stud)

    def display_student_details(self):
        """ display each student object """
        time.sleep(2)
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

STUDENT_LIST = []
if __name__ == "__main__":
    pstart = time.time()
    STUD1 = Student(1, "stud1", 10, 77.00)
    STUD2 = Student(2, "stud2", 11, 78.00)
    STUD3 = Student(3, "stud3", 12, 79.00)
    STUD4 = Student(4, "stud4", 13, 80.00)
    STUD5 = Student(5, "stud6", 14, 81.00)
    STUDENT_LIST.append(STUD1)
    STUDENT_LIST.append(STUD2)
    STUDENT_LIST.append(STUD3)
    STUDENT_LIST.append(STUD4)
    STUDENT_LIST.append(STUD5)
    print("time spend in create student list :-", time.time() - pstart)
    start = time.time()
    Student.update_percentage(STUDENT_LIST, 3, 92)
    print("time spend in update student list :-", time.time() - start)
    start = time.time()
    Student.delete_student_record(STUDENT_LIST, 5)
    print("time spend in delete student list :-", time.time() - start)
    print("overall program executed time ", time.time() - pstart)
