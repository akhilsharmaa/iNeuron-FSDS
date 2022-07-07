class Person:
    def __init__(self, name, surname, email, year ):
        self.name1 = name
        self.surname = surname
        self.email = email
        self.year = year

    def askName(self):
        self.name = input("Enter your name: ")


    def age(self):
        return 2021 - self.year

akhil = Person("Akhil", "Sharma", "anuj@gmail.com", 2001)
print(akhil.name1 + " " +  akhil.surname)
print(akhil.age());

akhil.askName();
print(akhil.name)