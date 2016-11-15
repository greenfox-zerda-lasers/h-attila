# Create a class what is capable of playing exactly one game of Cows and Bulls (CAB). The player have to guess a 4 digit
# number. For every digit that the player guessed correctly in the correct place, they have a “cow”. For every digit the
# player guessed correctly in the wrong place is a “bull.”

import random


# Feladatok
# - loopot összerakni
# - numbers generálása nem lehet ismétlődően
# - gui


class Cows_and_bulls():

    def __init__(self):

        self.status = 'playing'  # game status = (playing , finished)
        self.guess_list = []
        self.number_of_guess = 0
        self.numbers = []
        self.bulls = 0
        self.cows = 0


        [self.numbers.append(random.randint(0, 9)) for i in range(4)]
        print(self.numbers)

    def player_guess(self, guess):

        self.guess = guess
        self.guess_list = []

        for i in self.guess:
            if i in self.guess_list:
                print('Érvénytelen tipp, egy szám csak egyszer szerepelhet!')
            else:
                self.guess_list.append(i)

        for i in range(len(self.guess_list)):

            if self.guess_list[i] in self.numbers:
                if self.guess_list[i] == self.numbers[i]:
                    self.cows += 1
                else:
                    self.bulls += 1
        print('number: ', self.numbers, 'guess:', self.guess_list, 'bulls:', self.bulls, 'cows:', self.cows)


game = Cows_and_bulls()
game.player_guess('1243')
game.player_guess('')
