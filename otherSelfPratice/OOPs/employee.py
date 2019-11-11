class Employee():
    company_name = 'Calsoft'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__pf_number = '1234'
        print('Employee object created')
        # self.display_employee()

    def display_employee(self):
        print('Name: {}, Age: {}, Company: {}'.format(self.name, self.age, self.company_name))


class BavdhanEmployee(Employee):
    def __init__(self, name, age):
        print('Creaing Bavdhan employee')
        super().__init__(name, age)
        self.base_location = 'Bavdhan'

    def display_employee(self):
        print(f'Name: {self.name}, Age: {self.age}, Company: {self.company_name}, Base Location: {self.base_location}')


# # initializing the employee class
# empObj = Employee('Pranshu', 28)
#
# # empObj.display_employee()
# # print (empObj.company_name)
#

objSuma = Employee('Suma', 24)
objSuma.display_employee()

pranObj = BavdhanEmployee('Pranshu', 28)
pranObj.display_employee()
# print (pranObj.base_location)
# print (pranObj.__pf_number)
