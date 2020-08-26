# FUNCTIONS
# Creating a simple function
def greet_func():
    pass # using the pass keyword since there is no code - prevents errors
# Printing function - returns "None" since function is empty
print(greet_func())


# Creating a function with name parameter and code
def greeting_func(name):
    return f"Hola {name}!"
# Calling back greeting function and passing in argument for the name parameter
print(greeting_func("Luis"))


# Creating a function with default value when no name is entered
def greeting_2_func(name = "you"):
    return f"Hola {name}!"
# Printing this function will now print out the default value
print(greeting_2_func())


# Creating function that accepts any number of postional arguments and keyword arguments
def soccer_player_info(*args, **kwargs):
    print(args)
    print(kwargs)
# Calling definition and entering various positional and keyword arguments - returns
# pos. arguments as tuples and kwargs as dict. key-value pairs
soccer_player_info("Juventus", position= "Forward", foot="Left")

# Passing in lists to our soccer_player_info function
teams = ["Manchester United", "Portugal", "Sporting"]
info = {"position": "Forward", "foot": "Left"}
# Adding in "*" and "**" unpacks values in list and dict into our function
soccer_player_info(*teams, **info)