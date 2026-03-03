#Example1(Open the file "demofile.txt" and append content to the file)
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")
#open and read the file after the appending
with open("demofile.txt") as f:
    print(f.read())
#Example2(Open the file "dempfile.txt" and overwrite the content):
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")
#open and read the file after the overwriting:
with open("demofile.txt") as f:
    print(f.read())