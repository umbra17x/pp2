#Example1
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#Example2
for i in range(1,6):
    if i == 3:
        continue
    print(i)
#Example3
for x in range(1,11):
    if x % 2 == 0:
        continue
    print(x)
#Example4
fruits = ["apple","banana","cherry"]
for fruit in  fruits:
    if fruit == "banana":
        continue
    print(fruit)
#Example5
for letter in "Pyhton":
    if letter == "o":
        continue
    print(letter)