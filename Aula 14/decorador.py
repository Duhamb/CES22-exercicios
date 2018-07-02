# EXEMPLO DECORADOR #

class LancheComponent:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost

class Pao(LancheComponent):
    cost = 1.0

class Decorator(LancheComponent):
    def __init__(self, LancheComponent):
        self.component = LancheComponent
    def getTotalCost(self):
        return self.component.getTotalCost() + LancheComponent.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + ' ' + LancheComponent.getDescription(self)

class Hamburguer(Decorator):
    cost = 2.0
    def __init__(self, LancheComponent):
        Decorator.__init__(self, LancheComponent)

class Queijo(Decorator):
    cost = 0.5
    def __init__(self, LancheComponent):
        Decorator.__init__(self, LancheComponent)

class Tomate(Decorator):
    cost = 0.25
    def __init__(self, LancheComponent):
        Decorator.__init__(self, LancheComponent)

class Alface(Decorator):
    cost = 0.25
    def __init__(self, LancheComponent):
        Decorator.__init__(self, LancheComponent)

class Bacon(Decorator):
    cost = 0.5
    def __init__(self, LancheComponent):
        Decorator.__init__(self, LancheComponent)

class Maionese(Decorator):
    cost = 0.25
    def __init__(self, LancheComponent):
        Decorator.__init__(self, LancheComponent)

class Frango(Decorator):
    cost = 0.75
    def __init__(self, LancheComponent):
        Decorator.__init__(self, LancheComponent)

def main()
    LancheHamburguer = Queijo(Alface(Tomate(Hamburguer(Pao()))))
    print(LancheHamburguer.getDescription().strip() + ":$" + str(LancheHamburguer.getTotalCost()))

    LancheFrango = Maionese(Frango(Queijo(Queijo(Pao()))))

    print(LancheFrango.getDescription().strip() + ":$" + str(LancheFrango.getTotalCost()))

    LancheDuploHamburguerBacon = Bacon(Queijo(Hamburguer(Hamburguer(Pao()))))
    print(LancheDuploHamburguerBacon.getDescription().strip() + ":$" + str(LancheDuploHamburguerBacon.getTotalCost()))

if __name__ == "__main__":
    main()