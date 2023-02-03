def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
    # This is interesting. How does try work? What are its limits?

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))