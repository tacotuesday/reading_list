# Write a function that takes a list value as an argument and returns a string with all items separated
# by a comma and a space, with "and" inserted before the last item. Example has all strs but should work with any value
# passed to it.

# Accept a list value as an argument
# For all in list EXCEPT the last value, print the list item and ", ". I may be able to slice from list[0:(len(list)-1)].
# For the LAST item, print "and " + list[-1] + "."

spam = ['Frank', 'Reba', 42, 512]

