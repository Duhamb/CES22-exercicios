import abc

class Monster:

    __metaclass__ = abc.ABCMeta
    max_life = 100

    def __init__(self):
        self.life = max_life

    @classmethod
    def change_max_life(cls, max_life):
        cls.max_life = max_life

    @staticmethod
    def is_dead(life):
        if life <= 0:
            return True
        return False

    @abc.abstractmethod
    def get_hit(self):
        """"Under development"""
