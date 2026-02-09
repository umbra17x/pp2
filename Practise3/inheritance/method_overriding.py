#Example1
class Animal:
    def sound(self):
        print("Some sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c = Cat()
c.sound()
#Example2
class Person:
    def say(self):
        print("Hello")

class Child(Person):
    def say(self):
        print("Hi")

ch = Child()
ch.say()
#Example3
class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def draw(self):
        print("Drawing circle")

s = Circle()
s.draw()
#Example4
class Car:
    def move(self):
        print("Car moves")

class FastCar(Car):
    def move(self):
        print("Car moves fast")

f = FastCar()
f.move()