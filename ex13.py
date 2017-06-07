# This imports the sys module
# so we can take in args at the initialization.
from sys import argv

# Unpacks argv args into variables
script, first, second, third = argv

# Print out args passed in
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Now take in user input from command line
# as raw_input()
fourth = raw_input("Do you have a fourth variable? ")

print "Your fourth variable is:", fourth
