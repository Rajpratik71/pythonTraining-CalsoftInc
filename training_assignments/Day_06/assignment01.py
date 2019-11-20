'''
assignment 01 for static code analysis
'''
#!/usr/bin env python3

import sys

class Student:
    '''
    This is the class which holds information for students individually.
    '''
    def __init__(self, _name, _score):
        self.name = _name
        self.score = _score

    def __repr__(self):
        return f"{self.name} : {self.score}"


    def get_name(self):
        '''
        returns the name of the student
        '''
        return self.name

class Database:
    '''
    This is the class which manipulates the Students dictionary
    '''
    def __init__(self):
        self.database = {}
        self.key = 1

    def add_student(self, student):
        '''
        add student to the dictionary
        '''
        self.database[self.key] = student
        self.key += 1
        return True

    def delete_student(self, roll_no):
        '''
        delete the student entry
        '''
        if roll_no in self.database:
            self.database.pop(roll_no)
            return True
        return False

    def update_student(self, roll_no, student):
        '''
        update the student entry
        '''
        if roll_no in self.database:
            self.database[roll_no] = student
            return True
        return False

    def list_students(self):
        '''
        list the students from dictionary
        '''
        for key, student in self.database.items():
            print(f"{key} : {student}")

    def get_student(self, roll_no):
        '''
        returns the student W.R.T roll no
        '''
        return self.database.get(roll_no)


if __name__ == "__main__":
    DB = Database()
    while True:
        print("-------------------------------")
        print("1. Add new student")
        print("2. List all students")
        print("3. Get student by roll no")
        print("4. Update student by roll no")
        print("5. Delete student by roll no")
        print("6. Exit")
        print("-------------------------------")
        OPTION = int(input("Enter any one option given above: "))
        if OPTION == 1:
            NAME = input("Enter student name: ")
            SCORE = input("Enter student's score: ")
            DB.add_student(Student(NAME, SCORE))
        elif OPTION == 2:
            DB.list_students()
        elif OPTION == 3:
            ROLL_NO = int(input("Enter student roll no: "))
            STUDENT = DB.get_student(ROLL_NO)
            if STUDENT is not None:
                print(f"{ROLL_NO} : {STUDENT}")
            else:
                print("roll no {} does not exist".format(ROLL_NO))
        elif OPTION == 4:
            ROLL_NO = int(input("Enter student roll no: "))
            STUDENT = DB.get_student(ROLL_NO)

            if STUDENT is not None:
                print(f"current student information: {ROLL_NO} : {STUDENT}")
                NAME = input("Enter student name to update or press enter: ")
                SCORE = input("Enter student's score to update or press enter: ")

                if NAME != "":
                    STUDENT.name = NAME
                if SCORE != "":
                    STUDENT.score = SCORE
            else:
                print("roll no {} does not exist".format(ROLL_NO))


        elif OPTION == 5:
            ROLL_NO = int(input("Enter student roll no: "))

            IS_DELETED = DB.delete_student(ROLL_NO)

            if IS_DELETED:
                print("student has been deleted ")
            else:
                print("roll no {} does not exist".format(ROLL_NO))

        elif OPTION == 6:
            sys.exit()
