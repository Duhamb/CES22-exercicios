import turtle
import math

wn = turtle.Screen()
peter = turtle.Turtle()
peter.hideturtle()

list_of_pairs = [(0, 100), (90, 100), (45, 100/math.sqrt(2)), (90, 100/math.sqrt(2)), (45, 100),
                 (135, 100*math.sqrt(2)), (135, 100), (135, 100*math.sqrt(2))]

for (angle, distance) in list_of_pairs:
    peter.left(angle)
    peter.forward(distance)

wn.mainloop()