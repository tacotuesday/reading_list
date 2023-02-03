# Example of an import. In this case, we want random.randint().
# Al suggests the verbose form of import, but the other form is easier to use with long function names.
# import random
from random import randint as ri
for i in range(5):
    print(ri(1,10))
    # What other functions are in random?