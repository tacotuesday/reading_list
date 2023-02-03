from random import randint as ri
messages = ['It is certain.', 
    'It is decidedly so.',
    'Yes, definitely.',
    'Reply hazy, try again.',
    'Ask again later.',
    'Concentrate and ask again.',
    'My reply is no.',
    'Outlook not so good.',
    'Very doubtful.']

print(messages[ri(0, len(messages) - 1)])