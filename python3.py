from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font

board_width = 800
board_height = 400

root = Tk()
c = Canvas(root, width=board_width, height=board_height, background="sky blue")
c.create_rectangle(-5, board_height-100, board_width+5, board_height+5, fill="cyan", width=0)
c.create_oval(-80, -80, 120, fill='orange', width=0)
c.pack()

bolloon_color = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
bolloon_width = 45
egg_height = 55
bolloon_score = 10
bolloon_speed = 500
bolloon_interval = 4000

difficulty = 0.95

player_color = "blue"
player_width = 100
player_height = 100
player_startx = board_width/ 2 - player_width / 2
player_starty = board_height - player_height - 20
player_startx2 = player_startx + player_width
player_starty2 = player_starty +player_height