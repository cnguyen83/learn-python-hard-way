# Use escape sequences to format
# and escape special characters.
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Use triple double-quotes to create
# multi-line string with escaped characters.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Code to make a cool rotating line.
# Should not be run though since it doesn't terminate.
'''
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
'''

# Use triple single-quotes to create
# multi-line string.
skinny_cat = '''
This is a multi-line string.
That uses triple single-quotes.
'''

# Using a mix of escape characters
# and %r format characters.
tabby_cat = "Using %r to print %r and %r quotes." % ("%r", "\'", "\"")

# Using a mix of escape characters
# and using %s format characters.
tabby_cat2 = "Using %s to print %s and %s quotes." % ("%r", "\'", "\"")


print skinny_cat
print tabby_cat
print tabby_cat2
