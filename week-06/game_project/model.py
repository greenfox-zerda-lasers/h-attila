# model file for RPG game

from random import randint


class Character:

    def __init__(self, gameBoard):
        self.level = 1
        self.gameBoard = gameBoard
        self.posX = 0
        self.posY = 0

    def dice(self, number):
        return randint(1, number)

    def setStartPos(self):
        while True:
            self.posX = self.dice(10)-1
            self.posY = self.dice(11)-1
            if self.gameBoard[self.posY][self.posX] != 'w':
                break

    def move(self, direction):
        if direction == 'Up' and self.posY > 0 and self.gameBoard[self.posY-1][self.posX] != 'w':
            self.posY -= 1
        elif direction == 'Down' and self.posY < 10 and self.gameBoard[self.posY+1][self.posX] != 'w':
            self.posY += 1
        elif direction == 'Left' and self.posX > 0 and self.gameBoard[self.posY][self.posX-1] != 'w':
            self.posX -= 1
        elif direction == 'Right' and self.posX < 9 and self.gameBoard[self.posY][self.posX+1] != 'w':
            self.posX += 1


class Hero(Character):

    def __init__(self, gameBoard):
        super().__init__(gameBoard)
        self.key = False
        self.he = 20+3*self.dice(6)
        self.healthMax = 50
        self.dp = 2*self.dice(6)
        self.sp = 5+self.dice(6)
        self.direction = ''
        self.moveCounter = 0


class Enemy(Character):

    def __init__(self, gameBoard):
        super().__init__(gameBoard)
        self.key = False
        self.he = 2*self.level*self.dice(6)
        self.healthMax = 15
        self.dp = int(self.level/2)*self.dice(6)
        self.sp = self.level*self.dice(6)

    def enemyMove(self):
        i = 0
        while i > 0:
            random.choice(['left', 'right', 'up', 'down'])



class TheBoss(Character):

    def __init__(self, gameBoard):
        super().__init__(gameBoard)
        self.key = False
        self.he = 2*self.level*self.dice(6)+self.dice(6)
        self.healthMax = 25
        self.dp = int(self.level/2)*self.dice(6)+int(self.dice(6)/2)
        self.sp = self.level*self.dice(6)+self.level

