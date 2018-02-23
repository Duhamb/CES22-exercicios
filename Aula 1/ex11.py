import turtle
wn = turtle.Screen()
peter = turtle.Turtle()
peter.shape("turtle")

peter.hideturtle()
peter.left(36) #Ângulo inicial para a estrela

for i in range(5):
    #For para fazer os 5 traçados da estrela
    peter.forward(100)
    peter.left(144)

wn.mainloop()