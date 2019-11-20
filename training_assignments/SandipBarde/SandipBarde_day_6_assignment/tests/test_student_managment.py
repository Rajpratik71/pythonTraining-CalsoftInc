"""
class student
"""
import coverage
from unittest import TestCase, mock
from student_package.student_managment import Student


class StudentUnitTest(TestCase):
    def setUp(self) -> None:
        self.student = Student(1,"testname", 22, 77.77)
        self.student_list = []
        self.student_list.append(self.student)
    def tearDown(self) -> None:
        self.student = None

    def test_update_percentage(self):
        self.student.update_percentage(self.student_list, self.student.roll_number, 88.88)
        assert(self.student.percentage == 88.88)
    def test_delete_student_record(self):
        self.student.delete_student_record(self.student_list, 1)
        assert (len(self.student_list) == 0)
    def test_init(self):
        assert(self.student.roll_number == 1)