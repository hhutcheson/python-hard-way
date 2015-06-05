# Exercise 5 - Variables and String Formatting

my_name = 'Hunter J. Hutches'
my_age = 27
my_height_in = 60.0 # inches
my_height_cm = my_height_in * 2.54 # centimeters
my_weight_lbs = 192.0 # lbs
my_weight_kg = my_weight_lbs * 0.45 # kilograms
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "he's %d inches tall." % my_height_in
print "he's %d centimeters tall." % my_height_cm
print "He's %d pounds heavy." % my_weight_lbs
print "He's %d kilograms heavy." % my_weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are ususally %s depending on the coffee." % my_teeth

# tricky line
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height_in, my_weight_lbs, my_age + my_height_in + my_weight_lbs)
