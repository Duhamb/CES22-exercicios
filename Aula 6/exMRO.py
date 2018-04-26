class Shape:
    geometric_type = 'Generic Shape'

    def area(self): # This acts as placeholder for the interface
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:

    def plot(self, ratio, topleft):
        # Imagine some nice plotting logic here...

        print('Plotting at {}, ratio {}.'.format(topleft, ratio))

class Polygon(Shape, Plotter): # base class for polygons
    geometric_type = 'Polygon'

class Polygon2(Shape, Plotter): # base class for polygons
    geometric_type = 'Polygon'

class RegularPolygon(Polygon): # Is a Polygon
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularPolygon2(Polygon2): # Is a Polygon
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon): #Is a RegularPolygon
    geometric_type = 'Regular Hexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon2): # Is a RegularPolygon
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

class Extension_1(RegularHexagon, Square):
    geometric_type = 'None'

extension_1 = Extension_1(10)
print(extension_1.__class__.mro())


