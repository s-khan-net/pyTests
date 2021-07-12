class Person:
    def __init__(self):
        self.__age = 0
        self.__sex = "male"

    def set(self, age, sex):
        self.__age = age
        self.__sex = sex

    def __str__(self):
        return f"{self.__sex} of {self.__age} years"

    @classmethod
    def printsomeshit(self):
        print("printing some shit")
    
    @classmethod
    def make_maid(cls):
        return cls()


class Employee(Person):
    pass


p = Person()

print(p.__str__())
e = Employee()
e.set(23, "sex")
print(p.__str__())
print(e.__str__())
m = Person.make_maid()
print(m.__str__())
Person.printsomeshit()
