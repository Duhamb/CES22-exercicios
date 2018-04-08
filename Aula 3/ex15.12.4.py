import math

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def get_line_to(self, point2):

        a = (self.y - point2.y)/(self.x - point2.x)
        b = (point2.x*self.y - self.x*point2.y)/(point2.x - self.x)

        return (a, b)

print(Point(4, 11).get_line_to(Point(6, 15)))

#The method will fail when x1 = x2 (a-> oo), angle of 90 degrees.
