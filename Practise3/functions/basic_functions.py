#Example1(Creating function, we use 'def' keyword to define function)
def my_function():
    print("Hello from a function")
#Example2(to call a function, write its name followed by parentheses)
def my_function():
    print("Hello from a function")
my_function()
#Example3(with functions, we can write the code once and reuse it)
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
#Example4(also, we can call the same function multiple times)
def my_function():
    print("Hello from a function")
my_function()
my_function()
my_function()