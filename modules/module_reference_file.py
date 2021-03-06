# Created a function to find the index of a value in a sequence
def find_index(to_search, target):
    "find the index of a value in a sequence"
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


example_list = ["test", "test1", "test2"]

# Adding in pet functions
def bark(pet = "A dog"):
    print(pet, "Says Woof!")
def eat(pet = "A dog"):
    print(pet, "Eats a lot of food!")
def nap(pet = "A dog"):
    print(pet, "Sleeps all day")