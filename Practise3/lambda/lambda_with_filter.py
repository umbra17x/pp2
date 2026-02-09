#Example1(The filter() function creates a list of items for which a function returns True)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)
#Example2
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
#Example3
numbers = [5, 12, 7, 18, 3, 25]
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(greater_than_10)
#Example4
words = ["cat", "elephant", "dog", "tiger", "lion"]
long_words = list(filter(lambda x: len(x) > 4, words))
print(long_words)