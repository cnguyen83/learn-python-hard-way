# Define variables in order
# Make sure that if one variable name is defined using another variable
# the variable used to define it is defined earlier in the file.

# Variable names can represent the values
# Such that variable names are used in calculations
# This way a value does not need to be typed and changed
# in multiple different places. 

# Number of cars
cars = 100

# Seats available in a car
# Doesn't need to be floating point
# Seats in a car and people are never partial
space_in_a_car = 4.0

# Number of drivers
drivers = 30

# Number of people who need a ride
passengers = 90

# Using variables defined above
# figure out how many cars will remain idle
# since there is no one to drive them
cars_not_driven = cars - drivers

# The number of cars being driven
# is defined in terms of the number of drivers available.
# So the two variables are the same.
# Variables defined as such should make clear which
# one depends on another.
# Hence, drivers is defined first.
cars_driven = drivers

# How many people can be transported in total
# given number of cars being driven
# and their space capacity.
carpool_capacity = cars_driven * space_in_a_car

# If we want people split up among the cars evenly
# need to divide passengers by active cars.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
