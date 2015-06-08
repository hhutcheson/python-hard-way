# Exercise 16 - Reading and Writing Files

from sys import argv # Declare modules

script, filename = argv # Declare execute time variables

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # Request filename input

print "Opening the file..."
target = open(filename, 'w') # Open file specified

print "Truncating the file. Goodbye!"
target.truncate() # Create the file

print "Now I'm going to ask you for three lines."

# Input values for each line
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# Write the three lines
# target.write(line1) original line
# target.write("\n") original line
# target.write("%s\n" % line1) # line one attempt two
# target.write(line2)
# target.write("\n")
# target.write("%s\n" % line2) # line two attempt two
# target.write(line3)
# target.write("\n")
# target.write("%s\n" % line3) # line three attempt two
# FINAL CODE - all three write lines in one line of code
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# Close the file
print "And finally, we close it."
target.close()