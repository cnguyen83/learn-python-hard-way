# When printing, can escape characters.
# This lets us do formatting, such as newline or tab.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

# Using triple-double quotes (Westbrook!)
# lets us type things across multiple lines
# and have them to be printed in the format
# in which we type them.
# There's no need to do code indent within triple-double quotes?
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# This is an example of how spaces and tabs
# are read within triple-double quotes,
# like escape characters in a single-double quote.
print """
    This line is formatted out 4 spaces.
	This line is tabbed out.
\t This line uses a tab escape character.
This line is back to normal.

The above four lines are all within the same triple-double print statement.
"""
