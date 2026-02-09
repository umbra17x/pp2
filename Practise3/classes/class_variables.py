#Example1
class Dog:
    species = "Animal"   
print(Dog.species)
#Example2
class Dog:
    species = "Animal"

d1 = Dog()
print(d1.species)
#Example3
class Person:
    age = 18

p1 = Person()
p2 = Person()

print(p1.age)
print(p2.age)
#Example4
class Car:
    wheels = 4

Car.wheels = 6

c1 = Car()
print(c1.wheels)