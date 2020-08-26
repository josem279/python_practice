# CONDITIONALS
# Writing simple If statements using conditional operator
top_school = "UCF"

if top_school == "UCF":
    print("Conditional is true!")
else:
    print("Conditional is not true..")


# Activating else statement in function
if top_school == "MU":
    print("Conditional is true!")
else:
    print("Conditional is not true...")

# Activating an elif statement
top_school = "FSU"
if top_school == "UCF":
    print("Conditional is true!")
elif top_school == "FSU":
    print("Conditional is true, I guess")
else:
    print("Conditional is not true...")

# Creating if statements using conditional and boolean operators

# In this example both variables must be true due to "and" condition
food = "Pizza"
tasty = True

if food == "Pizza" and tasty:
    print("This food is tasty!")
else:
    print("Not a fan of this food")

# In this example either variable can be true due to "or" condition
food = "Tacos"
tasty = True

if food == "Pizza" or tasty:
    print("This food is tasty!")
else:
    print("Not a fan of this food")

# LOOPS AND ITERATIONS
# Simple loop to print all values in list
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# Using break keyword to end our loop once indicated number is found in nums list
for num in nums:
    if num == 3:
        print("Found the number!")
        break
    print(num)

# Using continue keyword to have our loop continue to run even after a number is found in nums list
for num in nums:
    if num == 3:
        print("Found the number!")
        continue
    print(num)

# Looping within a loop AKA nested loops - Chanting UCF 5 times
for num in nums:
    for letter in "UCF":
        print(num, letter)

# Indicating how many iterations of a loop we want using the range function, starting from 1
for n in range(1, 11):
    print(n)

# Creating a while loop - uses conditional operators to run loops
x = 15
while x < 16:
    print(x)
    x += 1 # Ensuring that loop ends once value is no longer less than 16 - prevents infinite loop

# Creating an infinite loop that is only broken when a condition is met and implementing break
x = 1
while True:
    if x == 4:
        break
    print(x)
    x += 1

