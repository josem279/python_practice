# STRINGS
# Assign string to message variable
message = "Hello World"

# Print welcome message
print(message)

# Print the length of message string
print(len(message))

# Print a slice of message string
print(message[6:])

# Print message in upper case and lower case
print(message.upper())
print(message.lower())

# Print out the number of times the letter "l" appear in message
print(message.count("l"))

# Replace letters in our message.
print(message.replace("H", "J"))

# Concatenating multiple strings
greeting = "Hey"
name = "John"
say_hey = greeting + ", " + name + ". Welcome to programming!"
print(say_hey)

# Printing greeting using f strings.
print(f"{greeting}, {name}. Welcome to programming!")

# Display name of all attributes and methods tied to a variable by showing the directory.
print(dir(message))

# To display infor on specific attribute or method use help function.
print(help(format))



# NUMERIC DATA
# Identifying whether data is an integer or a float
num = 3
num_2 = 12.5
print(type(num))
print(type(num_2))

# Using arithmetic operators
print(num + num_2)
print(num - num_2)
print(num * num_2)
print(num / num_2)
# floor division
print(num // num_2) 
# raise n to n2 power
print(num ** num_2) 
# mod operator, returns remainder after division
print(num % num_2) 

# Incrementing a variable
num_3 = -12.6
num_3 += 1
print(num_3)

# Print absolute value of number.
print(abs(num_3))

# Print out number to nearest integer
print(round(num_3))

# Print boolean value for comparison operators
num_4 = 31
num_5 = 50
print(num_4 == num_5)
print(num_4 != num_5)
print(num_4 > num_5)
print(num_4 < num_5)

# Cast string values into numeric values to perform arithmetic operations.
num_6 = "155"
num_7 = "143"
num_6 = int("155")
num_7 = int("143")
print(num_6 + num_7)