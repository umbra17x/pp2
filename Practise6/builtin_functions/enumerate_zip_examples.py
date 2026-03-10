# Example 1: enumerate list
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Example 2: enumerate starting from 1
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Example 3: zip two lists
names = ["Alice", "Bob", "Charlie"]
ages = [20, 25, 30]

for name, age in zip(names, ages):
    print(name, age)

# Example 4: zip numbers and letters
numbers = [1, 2, 3]
letters = ["a", "b", "c"]

for n, l in zip(numbers, letters):
    print(n, l)

# Example 5: zip and convert to list
list1 = [1, 2, 3]
list2 = ["x", "y", "z"]

result = list(zip(list1, list2))
print(result)