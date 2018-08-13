from PIL import Image
import turtle
import random
import math

screen = turtle.Screen()
screen_x = 700
screen_y = 1050
screen.setup(screen_x, screen_y)
'''
bg = Image.open('background.jpeg')
pix=bg.load()
bagr=bg.resize((700,1050),Image.ANTIALIAS)
bagr.save('thebackground.gif')
turtle.bgpic = ('thebackground.gif')
'''
player = turtle.Turtle()
pl = Image.open('papernobg.gif')
pn=pl.resize((50,50),Image.ANTIALIAS)
turtle.register_shape(pn)
player.shape(pn)


player.penup()
player.goto(0,480)

def move_left():
    x,y = player.pos()
    player.goto(x-20,y)

def move_right():
    x,y = player.pos()
    player.goto(x+20,y)

def move_down():
    x,y = player.pos()
    player.goto(x,y-10)

turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_down, "Down")
turtle.listen()



turtle.mainloop()
