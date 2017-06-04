# File to try variable names and print format characters
# For more string formatting references:  https://www.tutorialspoint.com/python/python_strings.htm


name = 'Zed A. Show'
age = 35 # not a lie
height_in = 74 #inches
weight_lbs = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Height and weight conversion
height_cms = height_in * 2.54
weight_kgs = weight_lbs * 0.45

# Print statements with variables
# Using format characters instead of embedding variable names
print "Let's talk about %s." % name

# Add print statement for height converted to cms
print "He's %d inches tall." % height_in
print "That's %d centimeters." % height_cms

# Add print statement for weight converted to kgs
print "He's %d pounds heavy." % weight_lbs
print "That's %d kilograms." % weight_kgs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (age, height_in, weight_lbs, age + height_in + weight_lbs)
