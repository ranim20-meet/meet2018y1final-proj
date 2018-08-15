from PIL import Image
import turtle
import random
import math

turtle.delay(0)

screen = turtle.Screen()
screen_x = 700
screen_y = 1050
screen.setup(screen_x, screen_y)
player = turtle.Turtle()


bg = Image.open('background.jpeg')
pix=bg.load()
bagr=bg.resize((700,1050),Image.ANTIALIAS)
bagr.save('thebackground.gif')
turtle.register_shape('thebackground.gif')
turtle.bgpic('thebackground.gif')

pl = Image.open('papernobg.gif')
pn=pl.resize((30,30),Image.ANTIALIAS)
pn.save('player.gif')
turtle.register_shape('player.gif')

screen.bgpic = ('thebackground.gif')
player.shape('player.gif')

player.penup()
player.goto(0,450)
'''
bins = player.clone()
binsim = Image.open('bins_crop.png')
pix = binsim.load()
binsimN = binsim.resize((700, 100),Image.ANTIALIAS)
binsimN.save('bins_crop_resize.gif')
turtle.register_shape('bins_crop_resize.gif')
bins.shape('bins_crop_resize.gif')

bins.penup()
bins.goto(0,-400)
'''
banana = player.clone()
banana.goto(0,-600)
bananaIM = Image.open('banana-peel.png')
pix = bananaIM.load()
RbananaIM = bananaIM.resize((30,30),Image.ANTIALIAS)
RbananaIM.save('banana.gif')
turtle.register_shape('banana.gif')
banana.shape('banana.gif')
#banana.speed(10)
#banana.ht()
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
paper_num = 0

def make_trash():
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
    #move_trash()
    #if len(paper_list) < 3:
     #       make_trash()

count = 0
def move_trash():
    global count, paper_num
    #while len(paper_list) > 0:
    for j in paper_list:  # for moving multiple papers
        #j.speed(3)
        x,y = j.pos()
        j.forward(10)
        print(j.pos())
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
                del j
            else:
                print('Game over!')
                quit()
    if paper_num<=4:
        make_trash()
    if count%20 == 0:
        make_banana()
    count += 1
    turtle.ontimer(move_trash, 100)
    #print("finish")

def check_len():
    if len(paper_list) < 3:
        make_trash()
        
def make_banana():
    bananat = banana.clone()
    #bananat.speed(3)
    bananat.shape('banana.gif')
    bananat.goto(random.randint(-15,15)*20, -400)
    bananat.left(90)
    bananat.st()
    paper_list.append(bananat)

#turtle.onkeypress(move_trash, "p")
turtle.onkeypress(make_trash, " ")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(make_banana, 'b')
turtle.listen()

move_trash()




turtle.mainloop()
