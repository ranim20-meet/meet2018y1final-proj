import turtle
turtle.bgcolor('black')
pic = turtle.clone()
turtle.register_shape('gameOverTrash.gif')
pic.shape('gameOverTrash.gif')
turtle.ht()
turtle.goto(-260,250)
turtle.color('red')
turtle.write('GAME OVER', font=('Ariel', 60, 'bold'))
