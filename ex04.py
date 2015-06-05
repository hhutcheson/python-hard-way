#Exercise 4 - Variables

cars = 100 # Variable - set the total number of cars (100)
space_in_a_car = 4.0 # Variable - set the number of seats (4) in each car
drivers = 30 # Variable - set the number of drivers (30)
passengers = 90 # Variable - set the number of passengers (90)
cars_not_driven = cars - drivers # Equation - cars without drivers are not driven
# cars_driven only works if drivers < cars
cars_driven = drivers # Equation - cars driven = number of drivers
# Equation - capacity = total driven cars * total spaces in each car (4)
carpool_capacity = cars_driven * space_in_a_car
# Equation - average passengers should be the same (or close to) 4.0
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
