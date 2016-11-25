from tkinter import *
from PIL import Image, ImageTk


class View:

    def __init__(self, game_board, hero):

        self.root = Tk()
        self.canvas = Canvas(self.root, width=720, height=795, bg='black')
        self.canvas_2 = Canvas(self.root, width=300, height=795, bg='white')
        self.canvas.pack(side=LEFT)
        self.canvas_2.pack(side=RIGHT)
        self.game_board = game_board
        self.hero = hero
        self.first_run = True
        self.hero_old_score = 0

        image_floor = Image.open("images/floor.png")
        image_wall = Image.open("images/wall.png")
        image_hero_down = Image.open("images/hero-down.png")
        image_hero_up = Image.open("images/hero-up.png")
        image_hero_left = Image.open("images/hero-left.png")
        image_hero_right = Image.open("images/hero-right.png")
        image_enemy = Image.open("images/skeleton.png")
        image_boss = Image.open("images/boss.png")
        image_enemy_profile = Image.open("images/enemy_zombi.jpeg")
        image_hero_profile = Image.open("images/hero_profile.jpeg")
        image_grave_stone = Image.open("images/grave_stone_5.jpg")
        image_coin = Image.open("images/coin.gif")
        image_key = Image.open("images/hero_key.jpg")

        self.photo_floor = ImageTk.PhotoImage(image_floor)
        self.photo_wall = ImageTk.PhotoImage(image_wall)
        self.photo_hero_down = ImageTk.PhotoImage(image_hero_down)
        self.photo_hero_down = ImageTk.PhotoImage(image_hero_down)
        self.photo_hero_up = ImageTk.PhotoImage(image_hero_up)
        self.photo_hero_left = ImageTk.PhotoImage(image_hero_left)
        self.photo_hero_right = ImageTk.PhotoImage(image_hero_right)
        self.photo_enemy = ImageTk.PhotoImage(image_enemy)
        self.photo_boss = ImageTk.PhotoImage(image_boss)
        self.image_enemy_profile = ImageTk.PhotoImage(image_enemy_profile)
        self.hero_profile = ImageTk.PhotoImage(image_hero_profile)
        self.image_grave_stone = ImageTk.PhotoImage(image_grave_stone)
        self.image_coin = ImageTk.PhotoImage(image_coin)
        self.image_key = ImageTk.PhotoImage(image_key)

    def draw(self):

        self.canvas.delete('all')
        self.text = self.canvas_2.create_text(180, 410, anchor="nw", fill="white", font="Arcade 25 italic bold", text=self.hero_old_score)

        if self.hero.event['direction'] == 'up':
            photo_hero_face = self.photo_hero_up
        elif self.hero.event['direction'] == 'left':
            photo_hero_face = self.photo_hero_left
        elif self.hero.event['direction'] == 'right':
            photo_hero_face = self.photo_hero_right
        else:
            photo_hero_face = self.photo_hero_down

        for j in range(11):
            for i in range(10):
                if self.game_board[j][i] == 'W':
                    self.canvas.create_image(i*72, j*72, anchor=NW, image=self.photo_wall)
                elif self.game_board[j][i] == 'H':
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.photo_floor)
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=photo_hero_face)
                elif self.game_board[j][i] == '0':
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.photo_floor)
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.photo_boss)
                elif self.game_board[j][i] in ['1', '2', '3']:
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.photo_floor)
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.photo_enemy)
                elif self.game_board[j][i] == 'c':
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.photo_floor)
#                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.image_coin)
                elif self.game_board[j][i] == '_':
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.photo_floor)

        self.text = self.canvas_2.create_text(70, 410, anchor="nw", fill="green", font="Arcade 25 italic bold", text="SCORE: ")
        self.text = self.canvas_2.create_text(180, 410, anchor="nw", fill="green", font="Arcade 25 italic bold", text=self.hero.power['score'])
        self.hero_old_score = self.hero.power['score']


    def mainloop(self):
        self.canvas.mainloop()

    def draw_info_screen(self, enemy):

        self.canvas_2.delete('all')
        self.text = self.canvas_2.create_text(2, 20, anchor="nw", fill="blue", font="Arcade 65 italic bold", text="HERO GAME")
        self.canvas_2.create_image(35, 90, anchor=NW, image=self.hero_profile)

        self.text = self.canvas_2.create_text(70, 330, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="HEATLH: ")
        self.text = self.canvas_2.create_text(70, 350, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="STRIKE: ")
        self.text = self.canvas_2.create_text(70, 370, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="DEFEND: ")
        self.text = self.canvas_2.create_text(70, 390, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="LEVEL: ")

        self.text = self.canvas_2.create_text(180, 330, anchor="nw", fill="red", font="Arcade 25 italic bold", text=self.hero.power['health'])
        self.text = self.canvas_2.create_text(180, 350, anchor="nw", fill="green", font="Arcade 25 italic bold", text=self.hero.power['strike'])
        self.text = self.canvas_2.create_text(180, 370, anchor="nw", fill="green", font="Arcade 25 italic bold", text=self.hero.power['defend'])
        self.text = self.canvas_2.create_text(180, 390, anchor="nw", fill="green", font="Arcade 25 italic bold", text=self.hero.power['level'])

        if self.hero.has_key:
            self.canvas_2.create_image(110, 420, anchor=NW, image=self.image_key)

        if not self.first_run:
            if enemy.power['health'] <= 0:
                self.canvas_2.create_image(15, 490, anchor=NW, image=self.image_grave_stone)
                enemy.power['health'] = 0
            else:
                self.canvas_2.create_image(15, 490, anchor=NW, image=self.image_enemy_profile)
                self.text = self.canvas_2.create_text(70, 710, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="HEATLH: ")
                self.text = self.canvas_2.create_text(70, 730, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="STRIKE: ")
                self.text = self.canvas_2.create_text(70, 750, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="DEFEND: ")
                self.text = self.canvas_2.create_text(70, 770, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="LEVEL: ")

                self.text = self.canvas_2.create_text(180, 710, anchor="nw", fill="red", font="Arcade 25 italic bold", text=enemy.power['health'])
                self.text = self.canvas_2.create_text(180, 730, anchor="nw", fill="green", font="Arcade 25 italic bold", text=enemy.power['strike'])
                self.text = self.canvas_2.create_text(180, 750, anchor="nw", fill="green", font="Arcade 25 italic bold", text=enemy.power['defend'])
                self.text = self.canvas_2.create_text(180, 770, anchor="nw", fill="green", font="Arcade 25 italic bold", text=enemy.power['level'])
        self.first_run = False

        self.canvas_2.update()

