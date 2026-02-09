#Example1(Create a class named MyClass, with a property named x)
class MyClass:
  x = 5
#Example2(Create an object named p1, and print the value of x)
p1 = MyClass()
print(p1.x)
#Example3(Delete the p1 object)
del p1
#Example4(Create three objects from the MyClass class)
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)