class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age


class LearnMixin:
    def __init__(self):
        self.workshops = []

    def enrol(self, course):
        self.workshops.append(course)


class TeacherMixIn:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Tutor(Person, LearnMixin, TeacherMixIn):
    def __init__(self, *args, **kargs):
        super(Tutor, self).__init__(*args, **kargs)


kshipra = Tutor('Kshipra', 'namjoshi', '25')

kshipra.enrol('Python')

kshipra.assign_teaching('ansible')

print(kshipra.assign_teaching)
