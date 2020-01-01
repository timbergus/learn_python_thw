def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"Multiply {a} * {b}")
    return a * b


def divide(a, b):
    print(f"Divide {a} / {b}")
    return a / b


print("Let's do some maths with just functions!")

age = add(30, 9)
height = subtract(200, 17)
weight = multiply(47, 2)
iq = divide(300, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit. Type it anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
