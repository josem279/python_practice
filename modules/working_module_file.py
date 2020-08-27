# MODULES
# Import desired modules - importing "module_reference" file - shortening name
import module_reference_file as mrf

# Created a list and calling in "find_index" function from imported module
florida_colleges = ["UCF", "FSU", "UF", "USF"]
college_index = mrf.find_index(florida_colleges, "UCF")
# Printing college_index gives us the index number of UCF
print(college_index)

# Calling in our pet functions
mrf.bark("Coco")
mrf.eat("Coco")
mrf.nap("Coco")

# Also possible to import function directly from module instead of all module file
# And importing list from module_reference file
from module_reference_file import find_index, example_list

# Gives us the same results
florida_colleges = ["UCF", "FSU", "UF", "USF"]
college_index = mrf.find_index(florida_colleges, "UCF")
print(college_index)
print(example_list)


# Importing the sys module to see path of current directory + extra directories we have acces to
import sys
print(sys.path)


# WORKING WITH MODULES FROM STANDARD PYTHON LIBRARY
# Importing random module and showing some examples
import random
# Randomly choosing a list item from the florida_colleges list
random_college = random.choice(florida_colleges)
print(random_college)
# Randomly generating a number between 0 and 1
print(random.random())


# Importing and using the math module
import math
# Using the ceil() and floor() methods to round floats to nearest integer value
print(math.ceil(3.61))
print(math.floor(3.61))
# math module allows us to perform trigonometry - example: converting degrees into radians
rads = math.radians(90)
print(rads)


# Importing the datetime module and calendar module
import datetime
import calendar
# Printing todays date using datetime module
today = datetime.date.today()
print(f" Today is {today}")
print(type(today))
# Using calendar module to see if the year is a leap year
print(calendar.isleap(2020))


# Importing the os module - gives us access to the operating system
import os
# Displays current working directory using os module
print(os.getcwd())