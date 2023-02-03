import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print('You typed ' + response + '.')
        sys.exit()
        # The original example had the previous two lines reversed. The program exited before printing.