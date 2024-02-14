class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setId(self, id):
        self.id = id

    def setDepartment(self, department):
        self.department = department

    def addEmployee(self, id):
        