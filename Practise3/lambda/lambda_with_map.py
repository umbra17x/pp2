#Example1(the map() function apllies a function to every item in an inerable)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#Example2
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)
#Example3
words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda x: x.upper(), words))
print(upper_words)
#Example4
numbers = [5, 10, 15]
added = list(map(lambda x: x + 10, numbers))
print(added)