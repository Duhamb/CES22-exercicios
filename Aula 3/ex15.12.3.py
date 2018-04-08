import math

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def slope_from_origin(self):
        return self.y/self.x

# Other statements outside the class continue below here.

print(Point(4, 10).slope_from_origin())
