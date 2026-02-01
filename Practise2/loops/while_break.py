#Example1
i = 1
while i < 0:
    print(i)
    if i == 3:
        break
    i += 1
#Example2
x = 0
while x < 10:
    print(x)
    if x == 5:
        break
    x += 1
#Example3
n = 3
while n >= -3:
    print(n)
    if n == 0:
        break
    n -= 1
#Example4
num = 1
while num <= 10:
    if num == 7:
        print("Found 7")
        break
    num += 1
#Example5
i = 1
while True:
    print(i)
    if i == 4:
        break
    i += 1