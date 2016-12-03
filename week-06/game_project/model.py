# model file for RPG game

import random


class Character:

    def __init__(self, gameBoard):
        self.level = 1
        self.gameBoard = gameBoard
        self.posX = 0
        self.posY = 0

    def dice(self, number):
        return random.randint(1, number)

    def setStartPos(self):
        while True:
            self.posX = self.dice(10)-1
            self.posY = self.dice(11)-1
            if self.gameBoard[self.posY][self.posX] != 'w':
                break

    def enemyMove(self):
        for i in range(10):
            direction = random.choice(['Left', 'Right', 'Up', 'Down'])
            if direction == 'Up' and self.posY > 0 and self.gameBoard[self.posY - 1][self.posX] != 'w':
                self.posY -= 1
                break
            elif direction == 'Down' and self.posY < 10 and self.gameBoard[self.posY + 1][self.posX] != 'w':
                self.posY += 1
                break
            elif direction == 'Left' and self.posX > 0 and self.gameBoard[self.posY][self.posX - 1] != 'w':
                self.posX -= 1
                break
            elif direction == 'Right' and self.posX < 9 and self.gameBoard[self.posY][self.posX + 1] != 'w':
                self.posX += 1
                break


class Hero(Character):

    def __init__(self, gameBoard):
        super().__init__(gameBoard)
        self.key = False
        self.he = 20+3*self.dice(6)
        self.healthMax = 50
        self.dp = 2*self.dice(6)
        self.sp = 5+self.dice(6)
        self.direction = 'Down'
        self.moveCounter = 0


    def heroMove(self):
        if self.direction == 'Up' and self.posY > 0 and self.gameBoard[self.posY-1][self.posX] != 'w':
            self.posY -= 1
        elif self.direction == 'Down' and self.posY < 10 and self.gameBoard[self.posY+1][self.posX] != 'w':
            self.posY += 1
        elif self.direction == 'Left' and self.posX > 0 and self.gameBoard[self.posY][self.posX-1] != 'w':
            self.posX -= 1
        elif self.direction == 'Right' and self.posX < 9 and self.gameBoard[self.posY][self.posX+1] != 'w':
            self.posX += 1

    def fightSkeleton(self, skeletonList):
        for i in range(len(skeletonList)):
            if self.posX == skeletonList[i].posX and self.posY == skeletonList[i].posY:
                if self.sp+2*self.dice(6) > skeletonList[i].dp:
                    print('hit skeleton')
                    skeletonList[i].he -= self.sp - skeletonList[i].dp
                    print('hero:', self.he, 'skeleton:', skeletonList[i].he)
                    if skeletonList[i].he <= 0:
                        if skeletonList[i].key:
                            self.key = True
                            print('hero has the key!')
                        skeletonList.remove(skeletonList[i])
                        break
                if skeletonList[i].sp+2*self.dice(6) > self.dp:
                    print('skeleton hit back')
                    self.he -= skeletonList[i].sp - self.dp

    def fightBoss(self, boss):
        if self.posX == boss.posX and self.posY == boss.posY:
            if self.sp+2*self.dice(6) > boss.dp:
                print('hit boss')
                print('hero:', self.he, 'boss:', boss.he)
                boss.he -= self.sp - boss.dp
                if boss.he <= 0:
                    pass
            if boss.sp+2*self.dice(6) > self.dp:
                print('boss hit back')
                self.he -= boss.sp - self.dp
            print('hero:', self.he, 'boss:', boss.he)


class Enemy(Character):

    def __init__(self, gameBoard):
        super().__init__(gameBoard)
        self.key = False
        self.he = 2*self.level*self.dice(6)
        self.healthMax = 15
        self.dp = int(self.level/2)*self.dice(6)
        self.sp = self.level*self.dice(6)


class TheBoss(Character):

    def __init__(self, gameBoard):
        super().__init__(gameBoard)
        self.key = False
        self.he = 2*self.level*self.dice(6)+self.dice(6)
        self.healthMax = 25
        self.dp = int(self.level/2)*self.dice(6)+int(self.dice(6)/2)
        self.sp = self.level*self.dice(6)+self.level
