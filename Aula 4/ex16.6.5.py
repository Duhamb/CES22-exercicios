class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

def is_colliding(rect1, rect2):
    collide_x = False
    collide_y = False
    x1, y1 = rect1.corner
    x2, y2 = rect2.corner

    difx = x2-x1
    dify = y2-y1

    if (rect1.width >= difx > 0) or (difx < 0 and rect2.width >= -difx) or difx == 0:
        collide_x = True

    # elif difx < 0 and rect2.width > -difx:
    #     collide_x = True

    if (rect1.height >= dify > 0) or (dify < 0 and rect2.height >= -difx) or dify == 0:
        collide_y = True

    # elif dify < 0 and rect2.height > -difx:
    #     collide_y = True

    if collide_x and collide_y:
        return True
    else:
        return False
