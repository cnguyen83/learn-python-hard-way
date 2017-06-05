# Variable to hold string to be printed.
# Consists entirely of formatters
formatter = "%r %r %r %r"

# Print ints, strings, bools, and even variables holding formatters.
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

# Notice that the third line will print with double quotes
# while the other lines will print with single quotes.
# Probably because the third line uses a single quote
# within the string itself.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
