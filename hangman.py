import random

Woerter = ['Krankenschwester']
'''Finanzen', 'Handschelle', 'Essig', 'Rotwein'''

Wort = random.choice(Woerter)
Wort = Wort.upper()
# gets a random word out of our list

newlist = list(Wort)
# splits the random words into a list
trys_left = 10
guessed_right = False
number_of_rights = 0




while True :
    trys_left = trys_left - 1
    my_input = str(input ('Gib einen Buchstaben ein oder loese das Wort: '))
    my_input = my_input.upper()

    if len(my_input) == 1:

        if my_input in newlist:
            number_of_rights = newlist.count(my_input)
            guessed_right = True

        else:
            guessed_right = False

        if guessed_right == True:
            trys_left = trys_left + 1
            print('Yes you guessed', number_of_rights, 'letter(s) right, you got ', trys_left, 'trys left. ')

        elif trys_left < 1:
            print('You loose! GIT GUD!!!')
            break

        elif guessed_right == False:
            print('no, thats wrong, guess again. You got ', trys_left, 'trys left.')


    elif len(my_input) == len(Wort):
        if Wort == my_input:
            print ('Holy Moly, you did it!')
            break

        else:
            print('The length of the word is right, change the word!')
