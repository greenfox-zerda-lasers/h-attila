import random
import game_map


class Character:

    def __init__(self, x, y, letter):

        self.event = {
            "x" : x,
            "y" : y,
            "direction": 'down',
            "can_move": True,
            "move_counter": 0,
            "battle_with": 'none',
            "sign" : letter
        }

        self.max_power = {
            "health" : 0,
            "max_health" : 0,
            "defend" : 0,
            "strike" : 0
        }

        self.power = {
            "health": 0,
            "defend": 0,
            "strike": 0,
            "level" : 1
        }
        self.has_key = False



class Hero(Character):

    def __init__(self, x, y, letter):
        super().__init__(x, y, letter)
        self.power = {
            "health": 30+random.randint(1,6)+random.randint(1,6)+random.randint(1,6),
            "max_health" : 50,
            "defend": 5 + random.randint(1,6)+random.randint(1,6),
            "strike": 1 + random.randint(3,6),
            "level" : 1,
            "score" : 0
        }


class Enemy(Character):

    def __init__(self, x, y, letter, has_key):
        super().__init__(x, y, letter)

        self.has_key = has_key
        self.active = False

        self.power = {
            "health": 12 + random.randint(1,6),
            "max_health" : 15,
            "defend": random.randint(1,6),
            "strike": random.randint(1,6),
            "level" : 1
        }


class TheBigBoss(Character):

    def __init__(self, x, y, letter):
        super().__init__(x, y, letter)

        self.power = {
            "health": 2 * random.randint(1,6) + random.randint(1,6) + 10,
            "max_health" : 30,
            "defend": random.randint(1,6) + random.randint(1,6),
            "strike": random.randint(1,6) + 5,
            "level" : 1
        }


class Move:

    def __init__(self, game_board, hero):
        self.game_board = game_board
        self.hero = hero

    def left_move(self, character):
        if character.event['x'] > 0 and self.game_board[character.event['y']][(character.event['x']-1)] not in ['H', 'W', '0', '1', '2', '3']:
            if self.game_board[character.event['y']][(character.event['x']-1)] == 'c' and character.event['sign'] == 'H':
                self.hero.power['score'] += 10
            self.game_board[character.event['y']][character.event['x']] = '_'
            character.event['x'] -= 1
            self.game_board[character.event['y']][character.event['x']] = character.event['sign']
            character.event['can_move'] = True
        else:
            character.event['can_move'] = False
            if character.event['x'] > 0 and character.event['sign'] == 'H' and self.game_board[character.event['y']][(character.event['x']-1)] in ['0', '1', '2', '3']:
                character.event['battle_with'] = int(self.game_board[character.event['y']][(character.event['x']-1)])

        character.event['direction'] = 'left'
        character.event['move_counter'] += 1

    def right_move(self, character):
        if character.event['x'] < 9 and self.game_board[character.event['y']][(character.event['x']+1)] not in ['H', 'W', '0', '1', '2', '3']:
            if self.game_board[character.event['y']][(character.event['x']+1)] == 'c' and character.event['sign'] == 'H':
                self.hero.power['score'] += 10
            self.game_board[character.event['y']][character.event['x']] = '_'
            character.event['x'] += 1
            self.game_board[character.event['y']][character.event['x']] = character.event['sign']
            character.event['can_move'] = True
        else:
            character.event['can_move'] = False
            if character.event['x'] < 9 and character.event['sign'] == 'H' and self.game_board[character.event['y']][(character.event['x']+1)] in ['0', '1', '2', '3']:
                character.event['battle_with'] = int(self.game_board[character.event['y']][(character.event['x']+1)])

        character.event['direction'] = 'right'
        character.event['move_counter'] += 1

    def up_move(self, character):
        if character.event['y'] > 0 and self.game_board[(character.event['y']-1)][character.event['x']] not in ['H', 'W', '0', '1', '2', '3']:
            if self.game_board[(character.event['y']-1)][character.event['x']] == 'c' and character.event['sign'] == 'H':
                self.hero.power['score'] += 10
            self.game_board[character.event['y']][character.event['x']] = '_'
            character.event['y'] -= 1
            self.game_board[character.event['y']][character.event['x']] = character.event['sign']
            character.event['can_move'] = True
        else:
            character.event['can_move'] = False
            if character.event['y'] > 0 and character.event['sign'] == 'H' and self.game_board[(character.event['y']-1)][character.event['x']] in ['0', '1', '2', '3']:
                character.event['battle_with'] = int(self.game_board[(character.event['y']-1)][character.event['x']])

        character.event['direction'] = 'up'
        character.event['move_counter'] += 1

    def down_move(self, character):
        if character.event['y'] < 9 and self.game_board[(character.event['y']+1)][character.event['x']] not in ['H', 'W', '0', '1', '2', '3']:
            if self.game_board[(character.event['y']+1)][character.event['x']] == 'c' and character.event['sign'] == 'H':
                self.hero.power['score'] += 10
            self.game_board[character.event['y']][character.event['x']] = '_'
            character.event['y'] += 1
            self.game_board[character.event['y']][character.event['x']] = character.event['sign']
            character.event['can_move'] = True
        else:
            character.event['can_move'] = False
            if character.event['y'] < 9 and character.event['sign'] == 'H' and self.game_board[(character.event['y']+1)][character.event['x']] in ['0', '1', '2', '3']:
                character.event['battle_with'] = int(self.game_board[(character.event['y']+1)][character.event['x']])
        character.event['direction'] = 'down'
        character.event['move_counter'] += 1

    def enemy_move(self, character):
        if character.power['health'] > 0:
            character.event['can_move'] = False
            i = 0
            while not character.event['can_move']:
                direction = random.choice(['left', 'right', 'up', 'down'])
                if direction == 'up':
                    self.up_move(character)
                elif direction == 'right':
                    self.right_move(character)
                elif direction == 'down':
                    self.down_move(character)
                else:
                    self.left_move(character)
                i += 1
                if i > 3:
                    break


class Battle:

    def __init__(self, game_board, hero, enemy_list):
        self.hero = hero
        self.enemy_list = enemy_list
        self.game_board = game_board

    def battle(self, enemy):
        self.enemy = enemy

        if self.enemy.power['defend'] >= self.hero.power['strike']:
            self.enemy.power['defend'] = self.hero.power['strike'] - 2
        if self.enemy.power['defend'] >= self.hero.power['strike']:
            self.enemy.power['defend'] = self.hero.power['strike'] - 2

        if self.hero.power['strike'] + 2*random.randint(1,6) > self.enemy.power['defend']:
            self.enemy.power['health'] = self.enemy.power['health'] + self.enemy.power['defend'] - self.hero.power['strike']

        if self.enemy.power['health'] <= 0:
            self.hero.power['health'] += random.randint(1,6)
            if self.hero.power['health'] > self.hero.power['max_health']:
                self.hero.power['health'] = self.hero.power['max_health']
            self.hero.power['defend'] += random.randint(2,5)
            self.hero.power['strike'] += random.randint(2,5)
            self.hero.power['level'] += 1
            if self.enemy.has_key:
                self.hero.has_key = True
            self.game_board[self.enemy.event['y']][self.enemy.event['x']] = '_'
            if self.hero.has_key and self.enemy_list[0].power['health'] <= 0:
                return True
        else:
            if self.enemy.power['strike'] + 2*random.randint(1,6) > self.hero.power['defend']:
                if self.hero.power['defend'] - self.enemy.power['strike'] < 0:
                    self.hero.power['health'] = self.hero.power['health'] + self.hero.power['defend'] - self.enemy.power['strike']
                else:
                    self.hero.power['health'] -= 2
