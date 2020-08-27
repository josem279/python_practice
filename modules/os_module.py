#OS MODULE

# Importing dependency - os module
import os
# Displaying all attributes and methods that os module gives us access to
#print(dir(os))

# Printing out the current working directory that we are in
print(os.getcwd())

# Navigating to a new directory
os.chdir("C:/Users/marti/data_analysis")
print(os.getcwd())
# Getting a list of all file in this new current directory
print(os.listdir())

# Creating a new folder in this new directory
#
os.mkdir("OS_EXample_")

