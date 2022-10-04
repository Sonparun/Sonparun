from random import randint
from readline import append_history_file
import pgzrun
width=640
height=480
apple=Actor('apple')
def draw():
    screen.clear()
    apple.draw()
def place_apple():
    apple.x=randint(10,600)
    apple.y=randint(10,400)
def on_ouse_down(pos):
    if apple.collidepoint(pos):
        print('Good Shot!')
        place_apple()
    else:
        print('YOu missed!')
place_apple()
pgzrun.go()