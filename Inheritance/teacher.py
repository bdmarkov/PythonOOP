from Inheritance.employee import Employee
from Inheritance.person import Person

class Teacher(Person, Employee):
    def teach(self):
        return f"teaching..."