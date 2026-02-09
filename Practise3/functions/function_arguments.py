#Example1(Here is a function with one argument)
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#Example2(If your function expects 2 arguments, you must call it with exactly 2 arguments)
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")
#Example3(Also, we can send arguments with the key = value syntax)
def my_function(animal, name):
    print("I have a",animal)
    print("My", animal + "'s name is", name)
my_function(animal = "dog", name = "Buddy")
#Example4(When you call a function with arguments without using keywords, they are called positional arguments.Positional arguments must be in the correct order)
def my_function(animal,name):
    print("I have a", animal)
    print("My", animal + "'s name is",name)
my_function("dog", "Buddy")
#Example5(You can mix positional and keyword arguments in a function call.)
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)