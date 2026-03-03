#Example1(remove the file "demofile.txt")
import os 
os.remove("demofile.txt")
#Example2(To avoid getting an error, you  might want to check if the file exists before you try to delete it)
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")