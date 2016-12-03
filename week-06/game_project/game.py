# RPG game

import model
import view
import map


class mainGameLoop:

    def __init__(self):
        self.gameBoard = map.mapLevel1
        self.drawing = view.Drawing()
        self.skeletonNumber = 3
        self.start()

    def start(self):
        self.skeletonList = []

        self.hero = model.Hero(self.gameBoard)
        self.hero.setStartPos()

        self.boss = model.TheBoss(self.gameBoard)
        self.boss.setStartPos()

        for i in range(self.skeletonNumber):
            self.skeletonList.append(model.Enemy(self.gameBoard))
            self.skeletonList[i].setStartPos()
        self.skeletonList[0].key = True

        self.drawing.map()
        for i in range(len(self.skeletonList)):
            self.drawing.skeleton(self.skeletonList[i])
        self.drawing.boss(self.boss)
        self.drawing.hero(self.hero)
        self.drawing.infoScreen()

        self.drawing.root.bind('<Left>', self.keyDetect)
        self.drawing.root.bind('<Right>', self.keyDetect)
        self.drawing.root.bind('<Up>', self.keyDetect)
        self.drawing.root.bind('<Down>', self.keyDetect)
        self.drawing.root.bind('<space>', self.keyDetect)

        self.drawing.mainloop()

    def keyDetect(self, keyEvent):
        if keyEvent.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.hero.direction = keyEvent.keysym
            self.hero.moveCounter += 1
            self.move()
        elif keyEvent.keysym == 'space':
            print('fight!')
            self.hero.fightSkeleton(self.skeletonList)
            self.hero.fightBoss(self.boss)

    def move(self):
        self.hero.heroMove()
        if self.hero.moveCounter % 2 == 0:
            if self.boss.he >= 0:
                self.boss.enemyMove()
            for i in range(len(self.skeletonList)):
                self.skeletonList[i].enemyMove()
        self.drawing.map()
        for i in range(len(self.skeletonList)):
            self.drawing.skeleton(self.skeletonList[i])
        if self.boss.he >= 0:
            self.drawing.boss(self.boss)
        self.drawing.hero(self.hero)
        self.drawing.infoScreen()
        self.checkWin()

    def checkWin(self):
        if self.boss.he <= 0 and self.hero.key:
            print('hello, gyoztem!')


################################ Main loop starts here ################################

game = mainGameLoop()
