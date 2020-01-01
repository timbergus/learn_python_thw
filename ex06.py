# This is two in binary.
types_of_people = 10
# This is the first part of the joke.
x = f"There are {types_of_people} types of people."

# This is a variable for the word "binary".
binary = "binary"
# This is a variable for the word "don't".
do_not = "don't"

# This is the second part of the joke.
y = f"Those who know {binary} and those who {do_not}."

print(x)  # This prints the first part of the joke.
print(y)  # This prints the second part of the joke.

# This tells the first part of the joke to a third person.
print(f"I said: {x}")
# This tells the second part of the joke to a third person.
print(f"I also said: '{y}'")

# This sets hilarious to False.
hilarious = False
# And now we ask if the joke is funny.
joke_evaluation = "Isn't that joke so funny!? {}"

# We print the answer to that question.
print(joke_evaluation.format(hilarious))

# Random string.
w = "This is the left side of..."
# Random string.
e = "a string with a rigth side."

# Concatenating two random strings.
print(w + e)
