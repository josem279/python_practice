# LISTS
# Create a list variable
courses = ["Math", "Physics", "French", "Biology", "Team Sports"]
courses_2 = ["Algebra", "Comp Sci"]
numbers = [50, 151, 54, 12, 1254, 481]
print(courses)

# Determine length of list variable
print(len(courses))

# Access second value in list using indexing
print(courses[1])

# Access last value in list using negative indexing
print(courses[-1])

# Access a range of values in courses list using slicing
print(courses[1:4]) # prints second to fourth values
print(courses[:3])  # prints all values up to third value
print(courses[2:])  # prints all values from the third value in list

# Add new course to end of our list
courses.append("German")
print(courses)

# Add new course as second value in list
courses.insert(1, "Geography")
print(courses)

# Add in values from courses_2 list to courses list
courses.extend(courses_2)
print(courses)

# Remove some of the courseload from our courses list
courses.remove("Team Sports") # Remove method lets us remove specific list item
print(courses)
courses.pop() # Pop method removes last item in list unless - Pop method also returns value that was removed
print(courses)

# Sorting lists...
courses.reverse() # Reverses order of items in list
print (courses)

courses.sort() # Sorts lists in alphabetical order or in ascending order by default
numbers.sort(reverse= True)
print(courses)
print(numbers)

# Print min, max, or sum of lists
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Print index value of value in list
print(courses.index("Geography"))

# Print boolean value to deterime if a value is in a list
print("French" in courses)

# Use loop to print all courses in courses list
for course in courses:
    print(course)

# Loop through each value in our list and print out index value and list value
# Use enumerate function to assign index value to list items and designate index start value
for index, course in enumerate(courses, start=1):
    print(index, course)

# Turning list of courses into string separated by certain value, ", " in this example
courses_str = ", ".join(courses)
print(courses_str)

# Splitting string values into list items based on separator
courses_list = courses_str.split(", ")
print(courses_list)

# TUPLES
# Work like lists but are immutable
tuple_1 = ("History", "Math", "Physics", "Biology")
tuple_2 = tuple_1

# SETS
# Priting sets will print out unique values
set_1 = {"History", "Math", "Physics", "Biology"}
set_2 = {"History", "Math", "Physics", "Biology", "Math"}

print(set_1)
print(set_2)

# DICTIONARIES
# Creating a dictionary holding inforamtion on an athlete using key-value pairs
athlete = {"Name": "Ryan", "Age": 24, "Sports": ["Football", "Wrestling"]}
print(athlete)

# Retrieving name information from our athlete dictionary
print(athlete["Name"])

# Retriving information from dictionary using get() method to prevent error message
print(athlete.get("Name"))

# Adding a new key-value pair to athlete dictionary
athlete["school"] = "UCF"
print(athlete)

# Updating values in athlete dictionary using the update method
athlete.update({"Name": "Ryan S.", "Team": "Knights"})
print(athlete)

# Deleting key-value pair in our athlete dictionary using delete method
del athlete["Age"]
print(athlete)

# Printing specific pieces of dictionary
print(len(athlete))
print(athlete.keys()) # Returns all dict keys
print(athlete.values()) # Returns all dict values

# Looping through and printing all key-value pairs in dictionary usitn items method
for key, value in athlete.items():
    print(key, value)