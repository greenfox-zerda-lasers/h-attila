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

        image_floor = Image.open("images/floor.png")
        self.photo_floor = ImageTk.PhotoImage(image_floor)
        image_wall = Image.open("images/wall.png")
        self.photo_wall = ImageTk.PhotoImage(image_wall)
        image_hero_down = Image.open("images/hero-down.png")
        self.photo_hero_down = ImageTk.PhotoImage(image_hero_down)
        image_hero_up = Image.open("images/hero-up.png")
        self.photo_hero_up = ImageTk.PhotoImage(image_hero_up)
        image_hero_left = Image.open("images/hero-left.png")
        self.photo_hero_left = ImageTk.PhotoImage(image_hero_left)
        image_hero_right = Image.open("images/hero-right.png")
        self.photo_hero_right = ImageTk.PhotoImage(image_hero_right)
        image_enemy = Image.open("images/skeleton.png")
        self.photo_enemy = ImageTk.PhotoImage(image_enemy)
        image_boss = Image.open("images/boss.png")
        self.photo_boss = ImageTk.PhotoImage(image_boss)
        image_enemy_profile = Image.open("images/enemy_zombi.jpeg")
        self.image_enemy_profile = ImageTk.PhotoImage(image_enemy_profile)
        image_hero_profile = Image.open("images/hero_profile.jpeg")
        self.hero_profile = ImageTk.PhotoImage(image_hero_profile)
        image_grave_stone = Image.open("images/grave_stone_.jpg")
        self.image_grave_stone = ImageTk.PhotoImage(image_grave_stone)

    def draw(self):

        self.canvas.delete('all')

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
                else:
                    self.canvas.create_image(i * 72, j * 72, anchor=NW, image=self.photo_floor)

    def mainloop(self):

        self.canvas.mainloop()

    def draw_info_screen(self, enemy):

        self.canvas_2.delete('all')

        self.text = self.canvas_2.create_text(15, 20, anchor="nw", fill="blue", font="Arcade 65 italic bold", text="RPG GAME")

        self.canvas_2.create_image(35, 90, anchor=NW, image=self.hero_profile)

        self.text = self.canvas_2.create_text(70, 330, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="HEATLH: ")
        self.text = self.canvas_2.create_text(70, 350, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="STRIKE: ")
        self.text = self.canvas_2.create_text(70, 370, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="DEFEND: ")
        self.text = self.canvas_2.create_text(70, 390, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="LEVEL: ")

        self.text = self.canvas_2.create_text(180, 330, anchor="nw", fill="red", font="Arcade 25 italic bold", text=self.hero.power['health'])
        self.text = self.canvas_2.create_text(180, 350, anchor="nw", fill="green", font="Arcade 25 italic bold", text=self.hero.power['strike'])
        self.text = self.canvas_2.create_text(180, 370, anchor="nw", fill="green", font="Arcade 25 italic bold", text=self.hero.power['defend'])
        self.text = self.canvas_2.create_text(180, 390, anchor="nw", fill="green", font="Arcade 25 italic bold", text=self.hero.power['level'])

        if not self.first_run:
            if enemy.power['health'] <= 0:
                self.canvas_2.create_image(25, 450, anchor=NW, image=self.image_grave_stone)
                enemy.power['health'] = 0
            else:
                self.canvas_2.create_image(25, 450, anchor=NW, image=self.image_enemy_profile)
                self.text = self.canvas_2.create_text(70, 690, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="HEATLH: ")
                self.text = self.canvas_2.create_text(70, 710, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="STRIKE: ")
                self.text = self.canvas_2.create_text(70, 730, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="DEFEND: ")
                self.text = self.canvas_2.create_text(70, 750, anchor="nw", fill="blue", font="Arcade 25 italic bold", text="LEVEL: ")

                self.text = self.canvas_2.create_text(180, 690, anchor="nw", fill="red", font="Arcade 25 italic bold", text=enemy.power['health'])
                self.text = self.canvas_2.create_text(180, 710, anchor="nw", fill="green", font="Arcade 25 italic bold", text=enemy.power['strike'])
                self.text = self.canvas_2.create_text(180, 730, anchor="nw", fill="green", font="Arcade 25 italic bold", text=enemy.power['defend'])
                self.text = self.canvas_2.create_text(180, 750, anchor="nw", fill="green", font="Arcade 25 italic bold", text=enemy.power['level'])
        self.first_run = False

        self.canvas_2.update()