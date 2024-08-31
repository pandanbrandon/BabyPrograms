"""
    Program: Magic Ate Ball
    By: yours truly
    Date: 8/28/24

    yuh.
"""

import random


# vars
responses = ['Maybe next time', 'Seek therapy', 'Nah.', 'With flying colors', 
             'Know your place', 'When was the last time you got laid?', 
             'mmmmm i du know', 'Smells like daddy issues', 'you go girl', 
             'slay queen', 'purrr', 'right on big dawg', ';)', 
             'I think you should get a dog', 'You got it in the bag', 'Oh yea',
             'Guaranteed']

active = True

# main
print("\n\nWhat's good cuh? \nYou got things on your mind?" + 
      "\nSpeak your mind and I'll try to ease your troubles")

while(active):
    print("\n\nAsk me a question\n")

    input("Type here: ")

    random.shuffle(responses)

    answer = random.choice(responses)

    print("\n" + str(answer))

    print("\nDo you want to ask another question?")
    
    userCont = input("\n'y' - yes or 'n' - no: ")

    if(userCont == 'n' or userCont == 'no'):
        active = False
        print("\n\nBye!")
