#Example1
class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()
#Example2
class Father:
    def skill1(self):
        print("Drive")

class Mother:
    def skill2(self):
        print("Cook")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()
#Example3
class Fly:
    def fly(self):
        print("Flying")

class Swim:
    def swim(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

d = Duck()
d.fly()
d.swim()
#Example4
class Read:
    def read(self):
        print("Reading")

class Write:
    def write(self):
        print("Writing")

class Student(Read, Write):
    pass

s = Student()
s.read()
s.write()