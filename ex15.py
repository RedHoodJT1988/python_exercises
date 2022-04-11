# using the sys module to import the argv package
from sys import argv

# create variables 'script' and 'filename' setting them to the arguments of argv
script, filename = argv

# create variable 'txt' and set its value to the filename argument
txt = open(filename)

# print message containing the name of the filename
print(f"Here's your file {filename}:")
# print out the contents of the file using the read() method
print(txt.read())

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())