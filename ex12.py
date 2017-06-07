# This does the exact same as ex11.py
# but the prompt question is used
# as an argument in raw_input()
# thus saving on "print" statements.
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
