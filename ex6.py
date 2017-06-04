# This first line shows that % char formatters
# do not require strictly a variable
# but allow you to change the printed value
# by editing the changing pieces at the end of the command.
# Additionally character formatters can be used
# in strings that are defined as variables,
# and their values can also be passed in
# in the same variable definition.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# These print strings that are stored in variables.
# In the case of y, the string prints strings inside of it.
print x
print y

# In these two lines, a string is put inside a string
# %r is used to print absolutely whatever is there
# whereas %s represents a string.
print "I said: %r." % x
print "I also said: '%s'." % y

# % char formatters can be used to print bools as well.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# A string can be defined with a character formatter in a variable,
# and the value passed into the formatter
# can be passed in whenever the string variable is actually used
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Just like concatenating a variable with a string,
# two variables that represent strings can be concatenated together.
print w + e
