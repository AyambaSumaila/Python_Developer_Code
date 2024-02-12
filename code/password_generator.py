import random
import string

print("Welcome to Password generator")

while True:
    for num in range(3):      

        adjective_list=[
            'sleepy', 'slow', 'smelly',
            'wet', 'orange', 'yellow',
            'green', 'blue', 'purple', 'fluffy',
            'white', 'proud', 'brave'
            ]


        nouns_list=[
            
            'apple', 'dinosaur', 'ball',
            'toaster', 'goat', 'dragon',
            'hammer', 'duck', 'dramma',
            'telephone', 'phone', 'teacher'
            ]

        sports_list=[
            'football', 'tennis', 'golf',
            'basketball', 'cricket', 'hocky'
            ]


        adjective=random.choice(adjective_list)
        noun=random.choice(nouns_list)

        sport=random.choice(sports_list)

        number=random.randrange(0, 100)
        special_char=random.choice(string.punctuation)

        password=adjective + noun + str(number) + sport + special_char
        print("Your new password is: %s" % password)
        
        response= input("Would you like another password? Type y or n:")
        
        if response == 'n':
            break
        


