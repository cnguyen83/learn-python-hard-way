# Use raw_input() to take in user input
# while having users enter their info
# on the same line as the question.
print "How old are you?", 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

# Print user input in regurgitation
# using %r so it keeps all the debugging format as is.
# Notice that if height is entered in n'm" format
# %r will print the \ to escape the single quote.
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Repeat the same
# but convert age and weight to int.

# Not doing safety checks yet to ensure
# user only enters numbers.
print "How old are you?", 
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = int(raw_input())


print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
