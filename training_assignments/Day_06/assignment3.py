import unittest

from assignment01 import Student, Database

class TestStudents(unittest.TestCase):
    def setUp(self) -> None:
        self.database = Database()
        
    def tearDown(self) -> None:
        del self.database

    def test_add_student(self):
        student = Student("Chris",90)
        self.assertTrue(self.database.add_student(student))
    
    def test_get_student(self):
        add_student = Student("Mark",99)
        self.database.add_student(add_student)
        student = self.database.get_student(1)
        self.assertIsInstance(student,Student)

    def test_delete_student(self):
        student = Student("Mark",99)
        self.database.add_student(student)
        self.assertTrue(self.database.delete_student(1))

if __name__ == "__main__":
    unittest.main()
