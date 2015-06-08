# Exercise 16a - Access file created in ex16.py
# Access ex16_test.txt


from sys import argv # Declare modules

script, filename = argv # Declare execution variables

txt = open(filename) # Open file specified

print txt.read() # Read/display specified file

txt.close() # Close specified file