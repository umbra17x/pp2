#Example1
i = 1
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
#Example2
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
#Example3
n = -2
while n < 3:
    n += 1
    if n == 0:
        continue
    print(n)
#Example4
count = 1
while count <= 5:
    if count == 4:
        count += 1
        continue
    print("Number:", count)
    count += 1
#Example5
num = -3
while num <= 3:
    num += 1
    if num < 0:
        continue
    print(num)