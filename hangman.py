import random

Woerter = ['Krankenschwester', 'Finanzen', 'Handschelle', 'Essig', 'Rotwein']

Wort = random.choice(Woerter)
Wort = Wort.upper()
# gets a random word out of our list

newstring = list(Wort)
# splits the random words into a list

Eingabe = str(input ('Gib einen Buchstaben ein oder loese das Wort: '))
Eingabe = Eingabe.upper()



while Eingabe != Wort or :
    for i in newstring:
        print (i)
