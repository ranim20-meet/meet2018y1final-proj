from PIL import Image
import turtle
import random
import math
import time
from pygame import mixer # Load the required library
turtle.delay(0)

screen = turtle.Screen()
screen_x = 700
screen_y = 1050
screen.setup(screen_x, screen_y)

run = True

def click(x,y):
    global run
    run = False


while run:
    def up():
        x,y = turtle.pos()
        turtle.goto(x,y+10)

    turtle.onkeypress(up, "Up")
    turtle.listen()
    turtle.speed(1)
    turtle.hideturtle()
    screen = turtle.Screen()
    screen.setup(800,800)
    yuval=turtle.clone()
    yuval.pensize(7)
    yuval.color('green')
    yuval.shape("arrow")
    caleb=turtle.clone()
    caleb.hideturtle()
    caleb.shape("arrow")
    screen.bgcolor("light green") 
    yuval.penup()
    yuval.goto(150,-300)
    yuval.left(180)
    yuval.pendown()
    yuval.forward(300)
    yuval.right(90)
    yuval.forward(500)
    yuval.left(90)
    yuval.forward(20)
    yuval.left(90)
    yuval.forward(35)
    yuval.left(90)
    yuval.forward(20)
    yuval.left(90)
    yuval.forward(50)
    yuval.right(90)
    yuval.forward(300)
    yuval.right(90)
    yuval.forward(15)
    yuval.right(90)
    yuval.forward(300)
    yuval.backward(20)
    yuval.right(90)

    for i in range(7):
        yuval.forward(15)
        yuval.right(90)
        yuval.forward(20)
        yuval.right(90)
        yuval.forward(15)
        yuval.left(90)
        yuval.forward(20)
        yuval.left(90)
    yuval.right(180)
    yuval.forward(35)
    yuval.left(90)
    yuval.forward(20)
    yuval.left(90)
    yuval.forward(35)
    yuval.left(90)
    yuval.forward(20)
    yuval.left(90)
    yuval.forward(500)
    caleb.penup()
    caleb.color('green')
    caleb.goto(-136,-30)
    caleb.pendown()
    caleb.write('Junk\nJourney', font = ('Ariel', 48, 'bold'))
    turtle.shape("square")
    turtle.penup()
    turtle.goto(-120,-90)
    turtle.write("Click on me to start!",font = ("Arial",20,"normal"))
    turtle.onclick(run)

player = turtle.Turtle()

x_image = 50
y_image = 50

bg = Image.open('background.jpeg')
pix=bg.load()
bagr=bg.resize((700,1050),Image.ANTIALIAS)
bagr.save('thebackground.gif')
turtle.register_shape('thebackground.gif')
turtle.bgpic('thebackground.gif')

pl = Image.open('papernobg.gif')
pn=pl.resize((x_image,y_image),Image.ANTIALIAS)
pn.save('player.gif')
turtle.register_shape('player.gif')

screen.bgpic = ('thebackground.gif')
player.shape('player.gif')

player.penup()
player.goto(0,450)

banana = player.clone()
banana.goto(0,-600)
bananaIM = Image.open('banana-peel.png')
pix = bananaIM.load()
RbananaIM = bananaIM.resize((x_image,y_image),Image.ANTIALIAS)
RbananaIM.save('banana.gif')
turtle.register_shape('banana.gif')
banana.shape('banana.gif')
#banana.speed(10)
#banana.ht()

can = player.clone()
canIM = Image.open('crushed-can.png')
pix = canIM.load()
RcanIM = canIM.resize((x_image,y_image),Image.ANTIALIAS)
RcanIM.save('can.gif')
turtle.register_shape('can.gif')
can.shape('can.gif')
can.ht()


def move_left():
    x,y = player.pos()
    player.goto(x-20,y)

def move_right():
    x,y = player.pos()
    player.goto(x+20,y)

def move_down():
    x,y = player.pos()
    player.goto(x,y-10)
i = 1
paper_list = []
paper_num = 0

def make_paper():
    global i
    global paper_list, paper_num
    paper = player.clone() #creates a clone of the player
    paper.shape('player.gif') #setting it's shape to paper
    #paper.speed(10)
    paper.penup() 
    paper.ht() #hide turtle
    paper.goto(random.randint(-15,15)*20,-400) #the x postition must be a
                                               #multiply of 20
    #paper.speed(3)
    paper.st()#show turtle
    paper.left(90)
    paper_list.append(paper)
    i+=1
    paper_num += 1
    print(paper_list)
score_stfu_rani_im_so_super_duper_creative = 0
count = 0
time = 100
def move_trash():
    global count, paper_num, score_stfu_rani_im_so_super_duper_creative, time
    for j in paper_list:  # for moving multiple papers
        #j.speed(3)
        x,y = j.pos()
        j.forward(10)
        #print(j.pos())
        if y > 500:
            if j.shape() == 'player.gif':
                paper_num -= 1
            j.ht()
            paper_list.remove(j)    
            print("finish")
        if player.pos() == j.pos():
            print("shape of trash: ",j.shape())
            if j.shape() == 'player.gif':
                j.ht() # make the paper disappear
                paper_list.remove(j)
                paper_num -= 1
                score_stfu_rani_im_so_super_duper_creative+=1
                time -= 7
                print(score_stfu_rani_im_so_super_duper_creative)
                del j
            else:
                turtle.textinput('Game Over!', 'You picked up the wrong kind of trash! your score is ' + str(score_stfu_rani_im_so_super_duper_creative) +". press 'ok' to finish the game.") 
                turtle.bye()
                os._exit(0)
    if paper_num<=4:
        make_paper()
    if count%20 == 0:
        make_trash(banana, banana)
    if count%30 == 0:
        make_trash(can, can)
    count += 1
    turtle.ontimer(move_trash, time)

        
def make_trash(kind, name):  #make trash acording to name&kind
    kind = banana.clone()
    if name == banana:
        kind.shape('banana.gif')
    if name == can:
        kind.shape('can.gif')
    kind.goto(random.randint(-15,15)*20, -400)
    kind.left(90)
    kind.st()
    paper_list.append(kind)

    
#turtle.onkeypress(make_trash, " ")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_down, "Down")
turtle.listen()

move_trash()

turtle.mainloop()
