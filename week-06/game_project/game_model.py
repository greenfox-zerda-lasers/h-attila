import random


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
            "defend" : 0,
            "strike" : 0
        }

        self.power = {
            "health": 0,
            "defend": 0,
            "strike": 0,
            "level" : 1
        }


class Hero(Character):

    def __init__(self, x, y, letter):
        super().__init__(x, y, letter)
        self.power = {
            "health": 20+random.randint(1, 6)+random.randint(1, 6)+random.randint(1, 6),
            "defend": random.randint(1, 6)+random.randint(1, 6),
            "strike": 2 + random.randint(1, 6),
            "level" : 1
        }


class Enemy(Character):

    def __init__(self, x, y, letter):
        super().__init__(x, y, letter)

        self.is_keyholder = False
        self.active = False

        self.power = {
            "health": 2 * random.randint(1 ,6),
            "defend": random.randint(1 ,6),
            "strike": random.randint(1 ,6),
            "level" : 1
        }


class TheBigBoss(Character):

    def __init__(self, x, y, letter):
        super().__init__(x, y, letter)

        self.power = {
            "health": 2 * random.randint(1 ,6) + random.randint(1 ,6),
            "defend": random.randint(1 ,6) + random.randint(1 ,6),
            "strike": random.randint(1 ,6) + 5,
            "level" : 1
        }


class Move:

    def __init__(self, game_board):

        self.game_board = game_board

    def left_move(self, character):
        if character.event['x'] > 0 and self.game_board[character.event['y']][(character.event['x']-1)] not in ['H', 'W', '0', '1', '2', '3']:
            self.game_board[character.event['y']][character.event['x']] = '_'
            character.event['x'] -= 1
            self.game_board[character.event['y']][character.event['x']] = character.event['sign']
            character.event['can_move'] = True
        else:
            character.event['can_move'] = False
            if character.event['x'] > 0 and character.event['sign'] == 'H' and self.game_board[character.event['y']][(character.event['x']-1)] in ['0', '1', '2', '3']:
                character.event['battle_with'] = int(self.game_board[character.event['y']][(character.event['x']-1)])
                print('Battle with magic: ', character.event['battle_with'])

        character.event['direction'] = 'left'
        character.event['move_counter'] += 1

    def right_move(self, character):
        if character.event['x'] < 9 and self.game_board[character.event['y']][(character.event['x']+1)] not in ['H', 'W', '0', '1', '2', '3']:
            self.game_board[character.event['y']][character.event['x']] = '_'
            character.event['x'] += 1
            self.game_board[character.event['y']][character.event['x']] = character.event['sign']
            character.event['can_move'] = True
        else:
            character.event['can_move'] = False
            if character.event['x'] < 9 and character.event['sign'] == 'H' and self.game_board[character.event['y']][(character.event['x']+1)] in ['0', '1', '2', '3']:
                character.event['battle_with'] = int(self.game_board[character.event['y']][(character.event['x']+1)])
                print('Battle with magic: ', character.event['battle_with'])

        character.event['direction'] = 'right'
        character.event['move_counter'] += 1

    def up_move(self, character):
        if character.event['y'] > 0 and self.game_board[(character.event['y']-1)][character.event['x']] not in ['H', 'W', '0', '1', '2', '3']:
            self.game_board[character.event['y']][character.event['x']] = '_'
            character.event['y'] -= 1
            self.game_board[character.event['y']][character.event['x']] = character.event['sign']
            character.event['can_move'] = True
        else:
            character.event['can_move'] = False
            if character.event['y'] > 0 and character.event['sign'] == 'H' and self.game_board[(character.event['y']-1)][character.event['x']] in ['0', '1', '2', '3']:
                character.event['battle_with'] = int(self.game_board[(character.event['y']-1)][character.event['x']])
                print('Battle with magic: ', character.event['battle_with'])

        character.event['direction'] = 'up'
        character.event['move_counter'] += 1

    def down_move(self, character):
        if character.event['y'] < 10 and self.game_board[(character.event['y']+1)][character.event['x']] not in ['H', 'W', '0', '1', '2', '3']:
            self.game_board[character.event['y']][character.event['x']] = '_'
            character.event['y'] += 1
            self.game_board[character.event['y']][character.event['x']] = character.event['sign']
            character.event['can_move'] = True
        else:
            character.event['can_move'] = False
            if character.event['y'] < 10 and character.event['sign'] == 'H' and self.game_board[(character.event['y']+1)][character.event['x']] in ['0', '1', '2', '3']:
                character.event['battle_with'] = int(self.game_board[(character.event['y']+1)][character.event['x']])
                print('Battle with magic: ', character.event['battle_with'])
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

    def rolling_dice(self, number):
        return random.randint(1, number)

    def battle(self, enemy):

        self.enemy = enemy
        print(self.game_board)
        print('attacker:', self.hero.power, 'defender:', self.enemy.power)
        if self.hero.power['strike'] + 2*self.rolling_dice(6) > self.enemy.power['defend']:
            self.enemy.power['health'] = self.enemy.power['health'] + self.enemy.power['defend'] - self.hero.power['strike']
            print('Successful hit! Attacker:', self.hero.power, 'defender:', self.enemy.power)
        else:
            print('Attack failed! Attacker:', self.hero.power, 'defender:', self.enemy.power)


        if self.enemy.power['health'] <= 0:
            print('Battle WIN, enemy dies! Attacker:', self.hero.power, 'defender:', self.enemy.power)
            self.hero.power['health'] += self.rolling_dice(6)
            self.hero.power['defend'] += self.rolling_dice(6)
            self.hero.power['strike'] += self.rolling_dice(6)
            self.hero.power['level'] += 1
            print('Hero level up! Attacker:', self.hero.power, 'defender:', self.enemy.power)
            self.game_board[self.enemy.event['y']][self.enemy.event['x']] = '_'

        else:
            print('Attack back!')
            if self.enemy.power['strike'] + 2*self.rolling_dice(6) > self.hero.power['defend']:
                self.hero.power['health'] = self.hero.power['health'] + self.hero.power['defend'] - self.enemy.power['strike']
                print('Successful hit! Attacker:', self.enemy.power, 'defender:', self.hero.power)
            else:
                print('Attack failed! Attacker:', self.enemy.power, 'defender:', self.hero.power)