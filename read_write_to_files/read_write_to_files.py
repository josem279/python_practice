# FILE OBJECTS

# Import dependencies
import os

print("Current directory is", os.getcwd())
# Creating variables for the files that we want to open/create
file_to_open = os.path.join("read_write_to_files", "example.txt")
file_to_write = os.path.join("read_write_to_files", "example2.txt")

print(file_to_open)
# Opening file with context manager so that we do not have to explicitly close the file
# throwing in r as mode to indicate read only and then reading in all contents of a file
with open(file_to_open, mode= "r") as testing_file:
    # testing_file_contents = testing_file.read()
    # print(testing_file_contents)


# If we do not want to read in all data we can also read in one line at a time
    # testing_file_contents = testing_file.readline()
    # print(testing_file_contents, end="")

    
# To prevent running out of memory or prevent using same line of code over and over, we can
# Use a for loop to print out each line in a file
    # for line in testing_file:
    #     print(line, end="")


# When working with big data sets we can use the read() method to print out data by
# a certain number of characters
    size_to_read = 100
    testing_file_contents = testing_file.read(size_to_read)
    while len(testing_file_contents) > 0:
        print(testing_file_contents, end="")
        testing_file_contents = testing_file.read(size_to_read)


# Writing to files
# We use the same context manager but indicate mode as "w"
# This file does not necessarily have to exist. If it is in "w" mode then file will be created
with open(file_to_write, mode= "w") as w_file:
    # Writing text to the file
    w_file.write("Test writing")
    # Adding in more than one write function to file add text to end point of previous write function
    w_file.write("Test writing")



# Creating a copy of read only text file by writing each line to a new "example_copy.txt" file
with open(file_to_open, "r") as rf:
    with open("example_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)




