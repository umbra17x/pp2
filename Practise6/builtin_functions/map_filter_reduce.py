from functools import reduce

# Example 1: filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Example 2: filter numbers greater than 3
numbers = [1, 2, 3, 4, 5]
greater_than_three = list(filter(lambda x: x > 3, numbers))
print(greater_than_three)

# Example 3: filter words longer than 3 letters
words = ["cat", "elephant", "dog", "lion"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)

# Example 4: reduce to sum numbers
numbers = [1, 2, 3, 4]
sum_numbers = reduce(lambda a, b: a + b, numbers)
print(sum_numbers)

# Example 5: reduce to multiply numbers
numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print(product)