import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
peter = turtle.Turtle()
peter.shape("turtle")
peter.color("blue")

for i in range(12):
    peter.penup()
    peter.forward(80)
    peter.pendown()
    peter.forward(20) #Traçado
    peter.penup()
    peter.forward(20)
    peter.stamp() #Tartaruga
    peter.left(180)
    peter.forward(120)
    peter.right(150)

wn.mainloop()


