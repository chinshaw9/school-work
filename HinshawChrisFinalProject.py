"""
Title:Snake
Author:Chris Hinshaw
Date Last Modified:12/2/2021
Description: A game of snake where the user controls a snake trying to eat apples. If the snake hits a side or runs into
itself, game over. Game is won when the snake fills the room.
"""
from tkinter import *

import random

root = Tk()
root.title('Do you want to play?')

root.geometry("300x300")






def clicker():

    my_frame = Frame(pop, bg="blue")
    my_fram.pack(pady=10)

    yes= button(my_frame, text="yes", command=lambda: choice("yes"), bg="orange")
    yes.grid(row=0, column=1)

    no = button(my_frame, text="no", command=lambda: choice("no"), bg="purple")
    no.grid(row=0, column=1)


myButton = Button(root, text='Yes', command=clicker)
myButton.pack(pady=50)

myButton2 = Button(root, text='No', command=clicker)
myButton2.pack(pady=50)

my_label = Label(root, text="")
my_label.pack(pady=50)


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

#defining classes and functions
class Snake:
    pass

class Food:
    pass

def next_turn():
    pass
def change_direction(n):
    pass

def check_collisions():
    pass
def game_over():
    pass

window = Tk()
window.title("Snake game")
window.resizable(True, True)

score = 0
direction = 'down'
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.mainloop()
