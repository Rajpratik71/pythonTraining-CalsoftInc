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

if __name__ == "__main__":
    STUDENT_LIST = []
    STUD1 = Student(1, "stud1", 10, 77.00)
    STUD2 = Student(2, "stud2", 11, 78.00)
    STUD3 = Student(3, "stud3", 12, 79.00)
    STUD4 = Student(4, "stud4", 13, 80.00)
    STUD5 = Student(5, "stud5", 14, 81.00)
    STUD6 = Student(6, "stud6", 15, 82.00)
    STUD7 = Student(7, "stud7", 16, 83.00)
    STUD8 = Student(8, "stud7", 17, 84.00)
    STUD9 = Student(9, "stud8", 18, 85.00)
    STUD0 = Student(0, "stud9", 19, 86.00)
    STUDENT_LIST.append(STUD1)
    STUDENT_LIST.append(STUD2)
    STUDENT_LIST.append(STUD3)
    STUDENT_LIST.append(STUD4)
    STUDENT_LIST.append(STUD5)
    STUDENT_LIST.append(STUD6)
    STUDENT_LIST.append(STUD7)
    STUDENT_LIST.append(STUD8)
    STUDENT_LIST.append(STUD9)
    STUDENT_LIST.append(STUD0)
    STUDENT_LIST_USING_LIST_COMPREHENSION = [stud for stud in STUDENT_LIST if stud.roll_number > 5 ]
    print("Student details with roll number greater than 5 using list comprehension ")
    for student in STUDENT_LIST_USING_LIST_COMPREHENSION:
        student.display_student_details()