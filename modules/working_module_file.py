# MODULES
# Import desired modules - importing "module_reference" file - shortening name
import module_reference_file as mrf

# Created a list and calling in "find_index" function from imported module
florida_colleges = ["UCF", "FSU", "UF", "USF"]
college_index = mrf.find_index(florida_colleges, "UCF")
# Printing college_index gives us the index number of UCF
print(college_index)

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

random_college = random.choice(florida_colleges)
print(random_college)

# Importing the math module
import math

rads = math.radians(90)
print(rads)

# Importing the datetime module and calendar module
import datetime
import calendar

# Printing todays date using datetime module
today = datetime.date.today()
print(today)

# Using calendar module to see if the year is a leap year
print(calendar.isleap(2020))

# Importing the os module - gives us access to the operating system
import os
# Displays current working directory using os module
print(os.getcwd())