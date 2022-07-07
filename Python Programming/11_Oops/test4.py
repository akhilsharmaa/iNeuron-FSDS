class Person:
    _name = "sudh";
    __surname = "Sharma"

# Inheriting From Person
class Employee(Person):
    pass

obj = Employee();
print(obj._name)

