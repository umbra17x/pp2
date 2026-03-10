import os

# Example 1: Print the current working directory
print("Current directory:")
print(os.getcwd())

# Example 2: List all files and folders in the current directory
# You should see demofile.txt here
print("\nFiles in current directory:")
print(os.listdir())

# Example 3: Create a new directory
os.mkdir("myfolder")
print("\nCreated folder 'myfolder'")

# Example 4: Change the current directory to 'myfolder'
os.chdir("myfolder")
print("Changed directory to:")
print(os.getcwd())

# Example 5: Go back to the parent directory
os.chdir("..")
print("Returned back to:")
print(os.getcwd())