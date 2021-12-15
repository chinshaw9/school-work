"""
Title:Snake
Author:Chris Hinshaw
Date Last Modified:12/14/2021
Description: Box will open asking user if they want to play the game Snake. A game of snake opens where the user controls a snake trying to eat apples. If the snake hits a side wall or runs into
itself, game over. Game is won when the snake fills the room.
"""
#imports a message box to ask if play wants to play
from tkinter import messagebox
result = messagebox.askyesno(
    title='Play?',
    message='Do you want to play Snake?',
    detail='click no to quit'
)
if not result:
    exit()
#if the play clicked yes the game window will open
from tkinter import *

import random


#sets siz of game board, speed of snake, starting body part count of snake, snake color, background color, and food color
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 70
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#40E0D0"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

#defining classes and functions

#defining snake class
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

#defining food class
class Food:
    def __init__(self):
        x = random.randint(0,(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag="food")

#defining
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction =="down":
        y += SPACE_SIZE
    elif direction =="left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text ="Score: {}".format(score))

        canvas.delete("food")

        food = Food()

    else:
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:

        window.after(SPEED, next_turn, snake, food)
def change_direction(new_direction):

   global direction

   if new_direction == 'left':
       if direction != 'right':
           direction = new_direction
   elif new_direction == 'right':
       if direction != 'left':
           direction = new_direction
   elif new_direction == 'up':
       if direction != 'down':
           direction = new_direction
   elif new_direction == 'down':
       if direction != 'up':
           direction = new_direction
#defining when the snake runs into a wall or istelf
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:

        return True
    elif y < 0 or y >= GAME_HEIGHT:

        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

#defining game over function
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text= "Game Over", fill = "red", tag="gameover")

#sets the window title and allows the size of the window to be changed
window = Tk()
window.title("Snake Game")
window.resizable(True, True)
#sets score to 0 and initial direction to down
score = 0
direction = 'down'
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
#binding arrow keys to movement
window.bind('<Left>', lambda  event: change_direction('left'))
window.bind('<Right>', lambda  event: change_direction('right'))
window.bind('<Up>', lambda  event: change_direction('up'))
window.bind('<Down>', lambda  event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
