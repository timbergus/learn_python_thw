name = 'Gustavo Muñoz'
age = 39
height = 1.83
weight = 94.5
eyes = 'brown'
teeth = 'ivory'
hair = 'black'

pounds_per_kg = 2.20462
inches_per_m = 39.3701

print(f"Let's talk about {name}")
print(f"He's {height} m tall.")
print(f"He's {height * inches_per_m} inches tall.")
print(f"He's {weight} kg heavy.")
print(f"He's {weight * pounds_per_kg} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky. Try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
