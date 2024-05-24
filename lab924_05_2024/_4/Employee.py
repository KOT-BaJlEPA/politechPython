
class Employee():
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def give_raise(self, incrase = 5000):
        self.salary = self.salary + incrase
        return self.salary

# fil = Employee("Filip", "Kirkorov", 70000)
# print(fil.salary)
# fil.give_raise()
# print(fil.salary)
# fil.give_raise(-30000)
# print(fil.salary)