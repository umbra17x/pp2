#Example1(Python also has a super() function that will make the child class inherit all the methods and properties from its parent)
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def fullname(self):
        return self.firstname + " " + self.lastname


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


s = Student("Emil", "Smith")
print(s.fullname())
#Example2
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

c = Child("Emil")
print(c.name)
#Example3
class Animal:
    def __init__(self, color):
        self.color = color

class Dog(Animal):
    def __init__(self, color):
        super().__init__(color)

d = Dog("brown")
print(d.color)
#Example4
class Person:
    def __init__(self, age):
        self.age = age

class Student(Person):
    def __init__(self, age):
        super().__init__(age)

s = Student(18)
print(s.age)