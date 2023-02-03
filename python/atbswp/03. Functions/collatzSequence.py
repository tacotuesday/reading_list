# What is it about return that seems to break the while loop?
# From kaggle: return is another keyword uniquely associated with functions. When Python encounters a return statement, it exits the function immediately, and passes the value on the right hand side to the calling context.
# How would I return all values to a data structure?

def collatz(number):
    
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            # print(number)
            # return number
        elif number % 2 == 1:
            number = 3 * number + 1
            # print(number)
            # return number
        print(number)
    # return number

print('Enter number:')
try:
    collatz(int(input()))
except ValueError:
    print('This only works with a number.')