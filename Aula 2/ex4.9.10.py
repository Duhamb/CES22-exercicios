import turtle
wn = turtle.Screen()
t = turtle.Turtle()

def star_draw():
    #Função que desenha uma estrela de lado 100
    t.hideturtle()
    for i in range(5):
        t.forward(100)
        t.right(144)

def next_star():
    t.penup()
    t.forward(350)
    t.right(144)
    t.pendown()

for i in range(5):
    star_draw()
    next_star()

wn.mainloop()