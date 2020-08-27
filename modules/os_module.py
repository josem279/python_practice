#OS MODULE

# Importing dependency - os module
import os
# Displaying all attributes and methods that os module gives us access to
#print(dir(os))

# Printing out the current working directory that we are in
print(os.getcwd())

# Navigating to a new directory - you will have to input your own
os.chdir("C:/Users/marti/data_analysis")
print(os.getcwd())
# Getting a list of all file in this new current directory
print(os.listdir())

# Creating a new folder in this new directory
# Using the mkdir() function only allows us to create one folder in current directory
os.mkdir("OS_Example_Dir")
# Using makedirs() function allows us to create a folder and other subfolder within that folder
os.makedirs("OS_Example_Dir2/Sub_Dir1")
print(os.listdir())

# Renaming a directory
os.rename("OS_Example_Dir", "OS_Example_Dir_1")
print(os.listdir())

# Removing directories
# Using rmdir() allows us to delete specific directory
os.rmdir("OS_Example_Dir_1")
# Using removedirs() function allows us to remove directory and intermediate directories
os.removedirs("OS_Example_Dir2/Sub_Dir1")
print(os.listdir())

# Useful functions with os.path:
# Using the join() function to get name of path for a file
file_path = os.path.join("C:/Users/marti/data_analysis", "functions.py")
print(file_path)
# Using the basename() function to obtain the name of a file - using a fake path and name
print(os.path.basename("/tmp/test.py"))
# Obtaining the directory name using the dirname() function
print(os.path.dirname("/tmp/test.py"))
# Get both the file name and dir name with the split function
print(os.path.split("/tmp/test.py"))
# Verify the existence of a path with the exists() function - should return false file/dir are fake
print(os.path.exists("/tmp/test.py"))



