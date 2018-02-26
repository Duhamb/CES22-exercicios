import turtle
wn = turtle.Screen()

def star_draw():
    #Função que desenha uma estrela de lado 100
    t = turtle.Turtle()
    t.hideturtle()
    for i in range(5):
        t.forward(100)
        t.right(144)

star_draw()

wn.mainloop()