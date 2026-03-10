import os

# Example 1: Create a new folder to store files
os.mkdir("files_folder")
print("Created 'files_folder'")

# Example 2: List files before moving
print("\nBefore moving:")
print(os.listdir())

# Example 3: Move demofile.txt into files_folder
# os.rename() can also be used to move files
os.rename("demofile.txt", "files_folder/demofile.txt")
print("Moved demofile.txt to files_folder")

# Example 4: List files after moving
print("\nAfter moving:")
print(os.listdir())

# Example 5: Move the file back to the original location
os.rename("files_folder/demofile.txt", "demofile.txt")
print("Returned demofile.txt back")