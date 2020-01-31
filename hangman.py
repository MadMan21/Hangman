import random
from list import words

Wort = random.choice(words)
Wort = Wort.upper()
# gets a random word out of our list

newlist = list(Wort)
# splits the random words into a list
trys_left = 50
guessed_right = False
number_of_rights = 0
guesslist = list('x'  * len(newlist))



while True :
    if trys_left < 1:
        print('You loose! The word was',(Wort), '. GIT GUD!!!')
        break

    if guesslist == newlist:
        print('You got it by guessing. Nice!')
        break


    my_input = str(input ('Enter a letter or solve the whole word. '))
    my_input = my_input.upper()
    print ('TRYS LEFT: ', (trys_left))



    if len(my_input) == 1:

        if my_input in newlist:
            index = newlist.index(my_input)
            number_of_rights = newlist.count(my_input)

            indizes = [i for i, value in enumerate(newlist) if value == (my_input)]
            for i in indizes:
                guesslist [i] = my_input


            guessstring = ''.join(guesslist)
            print (guessstring)
            print('Yes you guessed', number_of_rights, 'letter(s) right.')

        else:
            guessstring = ''.join(guesslist)
            print (guessstring)
            print('No, thats wrong.')
            trys_left = trys_left - 1





    elif len(my_input) == len(Wort):
        if Wort == my_input:
            trys_left = trys_left + 1
            print ('Holy Moly, you did it!')
            break

        else:
            print('The length of the word is right, change the word!')
