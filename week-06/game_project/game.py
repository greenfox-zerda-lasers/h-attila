# RPG game

import model
import view
import map
import random


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

        self.drawing.root.bind('<Left>', self.keyDetect)
        self.drawing.root.bind('<Right>', self.keyDetect)
        self.drawing.root.bind('<Up>', self.keyDetect)
        self.drawing.root.bind('<Down>', self.keyDetect)
        self.drawing.root.bind('<space>', self.keyDetect)

        self.drawing.mainloop()

    def keyDetect(self, keyEvent):
        self.hero.moveCounter += 1
        if keyEvent.keysym == 'Up':
            self.hero.move('Up')
            self.move()
        elif keyEvent.keysym == 'Down':
            self.hero.move('Down')
            self.move()
        elif keyEvent.keysym == 'Left':
            self.hero.move('Left')
            self.move()
        elif keyEvent.keysym == 'Right':
            self.hero.move('Right')
            self.move()
        elif keyEvent.keysym == 'space':
            pass

    def move(self):
        self.drawing.map()
        self.drawing.boss(self.boss)
        self.drawing.hero(self.hero)
        for i in range(len(self.skeletonList)):
            self.drawing.skeleton(self.skeletonList[i])


################################ Main loop starts here ################################

game = mainGameLoop()
