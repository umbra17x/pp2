#Example1
fruits = ["apple", "banana" , "cherry"]
for x in  fruits:
    print(x)
    if x == "banana":
        break
#Example2
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
#Example3
for i in range(1,6):
    if i == 3:
        break
    print(i)
#Example4
fruits = ["apple","banana","cherry"]
for fruit in fruits:
    if fruit == "banana":
        print("Found banana")
#Example5
for x in range(10):
    if x > 5:
        break
    print(x)
