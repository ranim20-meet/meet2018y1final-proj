from PIL import Image
import turtle
import random
import math
import time
from pygame import mixer # Load the required library
import os
turtle.delay(1)

screen = turtle.Screen()
screen_x = 700
screen_y = 1050
screen.setup(screen_x, screen_y)

run = True

# Opening screen
def click(x,y):
    global run
    run = False
    print('click')
turtle.delay(0)
turtle.speed(1)
turtle.hideturtle()
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
turtle.color('green')
turtle.penup()
turtle.goto(-120,-90)
turtle.write("Click on me to start!",font = ("Arial",20,"normal"))
    
while run:
    # do nothing
    turtle.st()
    turtle.onclick(click) # Wait until user click the tyrtle
    turtle.listen()
'''
run = True

color_list = ['brown','green','blue','yellow','red']
colorNum = 0

def click(x,y):
    global run
    run = False
    print('click')
    
def start_screen(color):

    turtle.hideturtle()
    screen = turtle.Screen()
    screen.setup(800,800)
    yuval=turtle.clone()
    yuval.pensize(7)
    yuval.color(color)
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
    caleb.color(color)
    caleb.goto(-136,-30)
    caleb.pendown()
    caleb.write('Junk\nJourney', font = ('Ariel', 48, 'bold'))
    turtle.shape("square")
    turtle.st()
    turtle.color('green')
    turtle.penup()
    turtle.goto(-120,-90)
    turtle.write("Click on me to start!",font = ("Arial",20,"normal"))


while run:
    # do nothing
    for color in color_list:
        start_screen(color)
    turtle.st()
    turtle.onclick(click) # Wait until user click the tyrtle
    turtle.listen()
'''   
turtle.clear()
caleb.clear()
yuval.clear()
turtle.ht()
screen.clear()
# Clears the opening screen
###############################################################
# insruction pop up screens
turtle.textinput('Instructions', 'Welcome to our game!')
turtle.textinput('Instructions','Move Right, Left and Down using the arrow keys')
turtle.textinput('Instructions', 'Take ONLY trash from your kind, or DIE!')
turtle.textinput('Instructions', 'When the recycling bins appear, try to get to the right bin for you.')
turtle.textinput('Instructions', 'Good Luck!')

turtle.delay(0)
player = turtle.Turtle()


x_image = 50
y_image = 50

# sets the bgpic
bg = Image.open('background.jpeg') # Sets bg to the image you want
pix=bg.load()  # Alow us to acces the pixels of the image
bagr=bg.resize((700,1050),Image.ANTIALIAS) # Resize the image to x_image, y_image
bagr.save('thebackground.gif') # Saves the new image. Remember to save as .gif!
turtle.register_shape('thebackground.gif') # Make thebackground.gif a valid turtle shape
turtle.bgpic('thebackground.gif') # Sets the backgound to thebackground.gif

pl = Image.open('papernobg.gif')
pn=pl.resize((x_image,y_image),Image.ANTIALIAS)
pn.save('player.gif')
turtle.register_shape('player.gif')

screen.bgpic = ('thebackground.gif')
player.shape('player.gif')

player.penup()
player.goto(0,450)

can = player.clone() # Makes a turtle
canIM = Image.open('crushed-can.gif') # Sets canIM to thr image you want
pix = canIM.load() # Alow us to acces the pixels of the image
RcanIM = canIM.resize((x_image,y_image),Image.ANTIALIAS) # Resize the image to x_image, y_image
RcanIM.save('can.gif') #saves the new image. Remember to save as .gif!
turtle.register_shape('can.gif') # Make can.gif a valid turtle shape
can.shape('can.gif') # Sets the shape of can to can.gif
can.ht() # Hides the turtle so we can't see it


banana = player.clone() # Makes a turtle
banana.goto(0,-600)
bananaIM = Image.open('banana-peel .gif')
pix = bananaIM.load()
RbananaIM = bananaIM.resize((x_image,y_image),Image.ANTIALIAS)
RbananaIM.save('banana.gif')
turtle.register_shape('banana.gif')
banana.shape('banana.gif')
#banana.speed(10)
#banana.ht()


glass = player.clone()
glassIM = Image.open('bottle.gif')
pix = glassIM.load()
RglassIM = glassIM.resize((x_image,y_image),Image.ANTIALIAS)
RglassIM.save('glass.gif')
turtle.register_shape('glass.gif')
glass.shape('glass.gif')
glass.ht()


bin_list = []
bin_pic = ['Blue_bin.gif', 'Brown_bin.gif', 'Yellow_bin.gif', 'Green_bin.gif', 'Red_bin.gif']
bin_open = ['blueBin.gif', 'brownBin.gif', 'yellowBin.gif', 'greenBin.gif', 'redBin.gif']
for i in range(5):
    bin_list.append(player.clone())
    canIM = Image.open(bin_open[i]) 
    pix = canIM.load() 
    RcanIM = canIM.resize((100,100),Image.ANTIALIAS)
    RcanIM.save(bin_pic[i]) 
    turtle.register_shape(bin_pic[i]) 
    bin_list[i].shape(bin_pic[i]) 
    bin_list[i].ht() 
    

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
    paper.st() #show turtle
    paper.left(90)
    paper_list.append(paper)
    i+=1
    paper_num += 1

score_stfu_rani_im_so_super_duper_creative = 0
count = 0
time = 100
xBin = 0
yBin = 0
bin_list_pos = []
def move_trash():
    global count, paper_num, score_stfu_rani_im_so_super_duper_creative, time, xBin, yBin, bin_list_pos
    kind_trash = player.shape()
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
        x1,y1 = player.pos()
        x2,y2 = j.pos()
        if abs(x1-x2) < 40 and abs(y1-y2) < 40:
            print("shape of trash: ",j.shape())
            if j.shape() == kind_trash:
                j.ht() # make the paper disappear
                paper_list.remove(j)
                paper_num -= 1
                score_stfu_rani_im_so_super_duper_creative+=1
                if time > 16:
                    time -= 7
                print(score_stfu_rani_im_so_super_duper_creative)
                del j
            else:
                j.ht()
                turtle.textinput('Game Over!', 'You picked up the wrong kind of trash! you scored ' + str(score_stfu_rani_im_so_super_duper_creative) +" points. press 'ok' to finish the game.") 
                screen.clear()
                player.ht()
                #turtle.bye()
            #while True:
                turtle1 = turtle.Turtle()
                screen1 = turtle.Screen()
                screen1.bgcolor('black')
                pic = turtle1.clone()
                pic.penup()
                turtle.register_shape('gameOverTrash.gif')
                pic.shape('gameOverTrash.gif')
                turtle1.hideturtle()
                turtle1.penup()
                turtle1.goto(-260,250)
                turtle1.color('red')
                turtle1.write('GAME OVER', font=('Ariel', 60, 'bold'))
                turtle1.color('red')
                turtle1.goto(-225,-270)
                turtle1.write('Click anywhere to close the game', font=('Ariel', 18, 'bold'))
                turtle.exitonclick()
    x1,y1 = player.pos()       
    if paper_num<=4:
        make_paper()
    if count%20 == 0:
        make_trash(banana, 'banana')
    if count%30 == 0:
        make_trash(can, 'can')
    if count%15 == 0:
        make_trash(glass,'glass')
    if count == 50:
        make_bins(int(-300))
    if count > 50:
        for i in range(len(bin_list_pos)):
            xBin, yBin = bin_list_pos[i]
            if abs(x1-xBin) < 40 and abs (y1-yBin) < 40:
                if bin_list[i].shape() == 'Blue_bin.gif':
                    turtle.textinput("Correct recycling bin!", 'You made it! good job! you scored ' + str(score_stfu_rani_im_so_super_duper_creative) + " points")
                    turtle.bye()
                    os._exit(0)
                else:
                    turtle.textinput('Game Over!', 'You went into the wrong recycling bin! you scored ' + str(score_stfu_rani_im_so_super_duper_creative) +" points. press 'ok' to finish the game.") 
                    screen.clear()
                    player.ht()
                    #turtle.bye()
                #while True:
                    turtle1 = turtle.Turtle()
                    screen1 = turtle.Screen()
                    screen1.bgcolor('black')
                    pic = turtle1.clone()
                    pic.penup()
                    turtle.register_shape('gameOverTrash.gif')
                    pic.shape('gameOverTrash.gif')
                    turtle1.hideturtle()
                    turtle1.penup()
                    turtle1.goto(-260,250)
                    turtle1.color('red')
                    turtle1.write('GAME OVER', font=('Ariel', 60, 'bold'))
                    turtle1.color('red')
                    turtle1.goto(-225,-270)
                    turtle1.write('Click anywhere to close the game', font=('Ariel', 18, 'bold'))
                    turtle.exitonclick()

                    
    count += 1
    turtle.ontimer(move_trash, time)

        
def make_trash(kind, name):  #make trash acording to name&kind
    kind = banana.clone()
    kind.shape(name + ".gif")
    kind.goto(random.randint(-15,15)*20, -500)
    kind.left(90)
    kind.st()
    paper_list.append(kind)


def make_bins(x):
    global xBin, yBin, bin_list_pos
    for Bin in bin_list:
        Bin.st()
        Bin.goto(x,-400)
        bin_list_pos.append(Bin.pos())
        x+=150
    
#turtle.onkeypress(make_trash, " ")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_down, "Down")
turtle.listen()

move_trash()

turtle.mainloop()
