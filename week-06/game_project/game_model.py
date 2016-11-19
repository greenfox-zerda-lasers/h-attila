# this is the model file for RPG game.
# It handle all data and functions, like movement, attack, hit, objects, etc.


class Entity():
    # it has soul and it can move on the board

    def __init__(self):

        self.power = {
            "helth" : 0
            "defend" : 0
            "strike" : 0
        }
        self.max_power = {
            "helth" : 0
            "defend" : 0
            "strike" : 0
        }
        self.level = 0
        self.position = {
            "pos_x" : 0,
            "pos_y" : 0
        }


class Hero(Entity):
    # the main character of the game

    def __init__(self):
        super(.__init__()):
        self.name = ''



class Enemy(Entity):
    # basic enemy character

    def __init__(self):

        self.is_keyholder = False



class TheBigBoss(Enemy):
    # main enemy

    def __init__(self):



class Board():
    # game area, and core functions

    def __init__(self):
        pass

    def create_board(self, size):

        for i in range(size):
            for j in range(size):
                row.append('')
            board.append(row)


    def read_from_file(self):
        pass

    def write_to_file(self):
        pass


class Bricks():
    # objects on the board

    def __init__(self):

        self.position = {
            "pos_x": 0,
            "pos_y": 0
        }
        self.strength = 2
        self.can_destroy_it = False