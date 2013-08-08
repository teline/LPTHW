# Imports the argument module
from sys import argv

# sets the arguments to the script name and name of text file
script, filename = argv

# opens the text file
txt = open(filename)

# prints the name of the file
print "Here's your file %r:" % filename
# prints the text inside the file
print txt.readline()
print txt.read()

# asks for the filename
print "Type the filename again:"
# user sets a new variable to a filename
file_again = raw_input("> ")

# opens the new filename
txt_again = open(file_again)

# read the contents of the new file
print txt_again.read()