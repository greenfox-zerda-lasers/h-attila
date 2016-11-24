# this is the controller file for RPG game. So this organize all the main functions.

import game_model
import game_view
import game_setup
import random


class GameMainControl:

    def __init__(self):

        self.game_level = 1
        self.game_board = game_setup.map_level_1

        self.hero = game_model.Hero(6, 1, 'H')

        self.enemy_0 = game_model.TheBigBoss(0, 6, '0')
        self.enemy_1 = game_model.Enemy(0, 0, '1')
        self.enemy_2 = game_model.Enemy(4, 0, '2')
        self.enemy_3 = game_model.Enemy(4, 4, '3')

        self.enemy_list = []
        self.enemy_list.append(self.enemy_0)
        self.enemy_list.append(self.enemy_1)
        self.enemy_list.append(self.enemy_2)
        self.enemy_list.append(self.enemy_3)

        self.move = game_model.Move(self.game_board)
        self.view = game_view.View(self.game_board, self.hero)
        self.battle = game_model.Battle(self.game_board, self.hero, self.enemy_list)

        self.view.root.bind('<Left>', self.left_key_detected)
        self.view.root.bind('<Right>', self.right_key_detected)
        self.view.root.bind('<Up>', self.up_key_detected)
        self.view.root.bind('<Down>', self.down_key_detected)

        self.view.draw()
        self.view.draw_info_screen(self.hero)
        self.view.mainloop()

    def left_key_detected(self, event):

        self.move.left_move(self.hero)
        if self.hero.event['battle_with'] != 'none':
            self.battle.battle(self.enemy_list[self.hero.event["battle_with"]])
            self.view.draw_info_screen(self.enemy_list[self.hero.event["battle_with"]])
            self.hero.event['battle_with'] = 'none'
        if self.hero.event['move_counter'] % 2 == 0:
            self.enemy_move()
        self.view.draw()

    def right_key_detected(self, event):

        self.move.right_move(self.hero)
        if self.hero.event['battle_with'] != 'none':
            self.battle.battle(self.enemy_list[self.hero.event["battle_with"]])
            self.view.draw_info_screen(self.enemy_list[self.hero.event["battle_with"]])
            self.hero.event['battle_with'] = 'none'
        if self.hero.event['move_counter'] % 2 == 0:
            self.enemy_move()
        self.view.draw()

    def up_key_detected(self, event):

        self.move.up_move(self.hero)
        if self.hero.event['battle_with'] != 'none':
            self.battle.battle(self.enemy_list[self.hero.event["battle_with"]])
            self.view.draw_info_screen(self.enemy_list[self.hero.event["battle_with"]])
            self.hero.event['battle_with'] = 'none'
        if self.hero.event['move_counter'] % 2 == 0:
            self.enemy_move()

        self.view.draw()

    def down_key_detected(self, event):

        self.move.down_move(self.hero)
        if self.hero.event['battle_with'] != 'none':
            self.battle.battle(self.enemy_list[self.hero.event["battle_with"]])
            self.view.draw_info_screen(self.enemy_list[self.hero.event["battle_with"]])
            self.hero.event['battle_with'] = 'none'
        if self.hero.event['move_counter'] % 2 == 0:
            self.enemy_move()

        self.view.draw()

    def enemy_move(self):
        for i in range(len(self.enemy_list)):
            self.move.enemy_move(self.enemy_list[i])


    def rolling_dice(self, number):
        return random.randint(1, number)


####################  Main Loop Starts Here ####################


GameLoop = GameMainControl()
