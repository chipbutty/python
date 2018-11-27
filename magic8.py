import random

messages = ['certain', 'decidedly so', 'yes definitely', 'reply hazy try again',
            'concentrate and ask again', 'my reply is no good', 'outlook not so good', 'doubtful']
print(messages[random.randint(0, len(messages))-1])
print (len(messages))