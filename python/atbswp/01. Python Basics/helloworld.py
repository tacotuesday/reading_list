# This program says hello and asks for my name. I added a couple of things to the example code.

print('Hello world!')
print('What is your name?')    # Ask for their name
myName = input()
print('It is good to meet you, ' + myName)
if len(myName) % 2 == 0:
    print('You have an even number of letters in your name!')
else:
    print('You have an odd number of letters in your name.')
print('What is your age?')    # Ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')