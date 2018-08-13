
from PIL import Image
import turtle
import random
import math

screen = turtle.Screen()
screen_x = 700
screen_y = 1050
screen.setup(screen_x, screen_y)


bg = Image.open('background.jpeg')
pix=bg.load()
bagr=bg.resize((700,1050),Image.ANTIALIAS)
bagr.save('thebackground.gif')
turtle.bgpic = ('thebackground.gif')

player = turtle.Turtle()
pl = Image.open('papernobg.gif')
pn=pl.resize((30,30),Image.ANTIALIAS)
pn.save('player.gif')
turtle.register_shape('player.gif')

screen.bgpic = ('thebackground.gif')
player.shape('player.gif')


player.penup()
player.goto(0,450)

def move_left():
    x,y = player.pos()
    player.goto(x-20,y)

def move_right():
    x,y = player.pos()
    player.goto(x+20,y)

def move_down():
    x,y = player.pos()
    player.goto(x,y-50)
i = 1
paper_list = []

def make_trash():
    global i
    global paper_list
    paper = player.clone() #creates a clone of the player
    paper.shape('player.gif') #setting it's shape to paper
    paper.speed(10)
    paper.penup() 
    paper.ht() #hide turtle
    paper.goto(random.randint(-15,15)*20,-400) #the x postition must be a
                                               #multiply of 20
    paper.speed(3)
    paper.st()#show turtle
    paper.left(90)
    paper_list.append(paper)
    i+=1
    print(paper_list)
    move_trash()
    make_trash()

def move_trash():
    for j in paper_list:  # for moving multiple papers
        x,y = j.pos()
        print(j.pos())
        while y < 500:  # while the paper is inside the screen
            j.forward(50)
            x,y = j.pos()
            print("poses: ",player.pos(),j.pos())
            if player.pos() == j.pos(): 
                j.ht() # make the paper disappear
        print("finish")
        j.ht() #make the paper disappear even if it was not colected
        
        
#turtle.onkeypress(move_trash, "p")
turtle.onkeypress(make_trash, " ")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_down, "Down")
turtle.listen()


turtle.mainloop()
