import turtle
wn = turtle.Screen()
peter = turtle.Turtle()
peter.shape("turtle")

def voltar():
    #Função que faz a tartaruga peter voltar de 200
    peter.penup()
    peter.left(180)
    peter.forward(200)
    peter.right(180)
    peter.pendown()

voltar()

for i in range(3):
    #For para a tartaruga fazer um triângulo equilátero de lado 100
    peter.forward(100)
    peter.left(120)

peter.penup()
peter.forward(200)
peter.pendown()

for i in range(4):
    #For para a tartaruga fazer um quadrado de lado 100
    peter.forward(100)
    peter.left(90)

peter.penup()
peter.right(90)
peter.forward(200)
peter.left(90)
peter.pendown()

for i in range(6):
    #For para a tartaruga fazer um hexágono regular de lado 70
    peter.forward(70)
    peter.left(60)

voltar()

for i in range(8):
    #For para a tartaruga fazer um octógono regular de lado 50
    peter.forward(50)
    peter.left(45)

wn.mainloop()