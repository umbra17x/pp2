#Example1(return an iterator from a tuple, and print each value)
mytuple = ("apple", "banana" , "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
#Example2(atrings are also iterable objects, containing a sequance of characters)
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#Examople3(Iterate the values of a tuple)
mytuple = ("apple", "banana" , "cherry")
for x in mytuple:
    print(x)
#Example4(Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.))
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#Example5(A generator function is a special type of function that returns an iterator object.Instead of using return to send back a single value, generator functions use yield to produce a seriesof results over time)
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1
ctr = fun(5)
for n in ctr:
    print(n)
#Example6(we will create a simple generator that will yeild three integers.)
def fun():
    yield 1
    yield 2
    yield 3
for val in fun():
    print(val)
#Example7(We will create a generator object that will print the squares of integers between tange of 1 to 6(exclusive))
sq = (x*x for x in range(1,6))
for i in sq:
    print(i)
