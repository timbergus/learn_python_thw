# Number of available cars.
cars = 100
# People that can travel in each car.
space_in_a_car = 4.0
# Number of drivers.
drivers = 30
# Number of passengers.
passengers = 90
# The number of cars that has no driver.
cars_not_driven = cars - drivers
# The number of cars that are going to be used.
cars_driven = drivers
# The number of available places.
carpool_capacity = cars_driven * space_in_a_car
# The average number of passangers per car.
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
