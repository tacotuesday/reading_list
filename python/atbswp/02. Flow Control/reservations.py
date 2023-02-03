name = ''
while not name:
    print('Enter your name:')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())  
# I should validate the numOfGuests input. Entering no values returns a "ValueError: invalid literal for int()..." error.
# Is that because '' is considered False and there are no conditions to handle a lack of guests?
# The digit O is a valid entry.
if numOfGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')