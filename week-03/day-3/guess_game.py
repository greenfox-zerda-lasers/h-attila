
import random


limit = int(input("Add meg a felső határt [0, ... ]: "))

if limit < 10:
    print("Na, neeee, ennél nehezebb legyen a feladat. :))))")

else:
    number = int(random.randint(0, limit))
    tipps = 1
    guess = 0

    while number != guess:
        guess = int(input("Add meg a tipped: "))
        if guess == number:
            print("Gratulálok, eltaláltad", tipps, "próbával!")
            break
        elif guess < number:
            print("Az én számom nagyobb!")
        else:
            print("Az én számom kisebb!")
        tipps += 1