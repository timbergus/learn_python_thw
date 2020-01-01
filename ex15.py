# from sys we import argv to be used.
from sys import argv

# Here we deconstruct argv in two variables.
script, file_name = argv

# This line opens a file into a variable.
txt = open(file_name)

# And now we print the file using "read".
print(f"Here's your file {file_name}:")
print(txt.read())

txt.close()

# And we do the same but getting the file name
# from a console input.
print("Type the file name again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
