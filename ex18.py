# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# OK, that *args is actually pointless. We can just do this.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This one just takes one argument.
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no parameters.
def print_none():
    print("I got nothin'.")

print_two("Gustavo", "Muñoz")
print_two_again("Gustavo", "Muñoz")
print_one("First!")
print_none()

