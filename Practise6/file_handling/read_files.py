#Example1(The open() function returns a file object, which has a read() method for reading the contest on the file)
f = open("demofile.txt")
print(f.read())
#Example2(You can also use the with statement when opening a file.Then you do not have to worry about closing your files, the with statement takes care of that.)
with open("demofile.txt") as f:
    print(f.read())
#Example3(Close the file when you are finished with it)
f = open("demofile.txt")
print(f.readline())
f.close()
#Example4(By default the read() method returns the whole text, but you can also specify how many characters you want to return)
with open("demofile.txt") as f:
    print(f.read(5))
#Example5(By calling readline() two times, you can read the two first lines)
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
#Example6(Loop through the file line by line)
with open("demofile.txt") as f:
    for x in f:
        print(x)