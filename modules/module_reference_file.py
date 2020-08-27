# Created a function to find the index of a value in a sequence
def find_index(to_search, target):
    "find the index of a value in a sequence"
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


example_list = ["test", "test1", "test2"]