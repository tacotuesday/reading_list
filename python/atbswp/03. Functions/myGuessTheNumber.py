# I wanted to reverse-engineer the number-guessing game before seeing the solution.
# I didn't know that there was a limit to the number of guesses, but otherwise I got it.

from random import randint as ri
targetNumber = ri(1,20)
guessIteration = 0
guessNumber = None
print('I am thinking of a number between 1 and 20.')
while guessNumber != targetNumber:
    guessIteration = guessIteration + 1
    print('Take a guess.')
    guessNumber = int(input())
    if guessNumber == targetNumber:
        if guessIteration == 1:
            print('Good job! You got it in 1 guess!')
        else:
            print('Good job! You got it in ' + str(int(guessIteration)) + ' guesses.')
    elif guessNumber < targetNumber:
        print('Your guess is too low')
    elif guessNumber > targetNumber:
        print('Your guess is too high.')

# This works, but I could refactor it with a function.
# I think I could make the while logic a function?
# I tried to make the entire thing a function, but the while loop was infinite.