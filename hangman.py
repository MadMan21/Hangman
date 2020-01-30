import random

Woerter = ['Krankenschwester']
'''Finanzen', 'Handschelle', 'Essig', 'Rotwein'''

Wort = random.choice(Woerter)
Wort = Wort.upper()
# gets a random word out of our list

newlist = list(Wort)
# splits the random words into a list
counter = 0
guessed_right = False




while True :
    counter = counter + 1
    my_input = str(input ('Gib einen Buchstaben ein oder loese das Wort: '))
    my_input = my_input.upper()

    for item in newlist:
        if my_input == item:
            number_of_rights = newlist.count(my_input)
            guessed_right = True
        elif item != my_input:
            guessed_right = False

    if guessed_right == True:
        print('yes')

    elif guessed_right == False:
        print('no')



    '''if Eingabe in newstring:
        print('yeah')


    elif Eingabe not in newstring:
        print('Auweh')'''
