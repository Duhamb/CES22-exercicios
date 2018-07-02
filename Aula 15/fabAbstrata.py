# EXEMPLO FÁBRICA ABSTRATA #

import abc

class BasePizza(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Pizza(self):
        pass

    @abc.abstractmethod
    def DietPizza(self):
        pass

class Margherita(BasePizza):
    def Pizza(self):
        return PizzaMargherita()

    def DietPizza(self):
        return DietPizzaMargherita()

class Chocolate(BasePizza):
    def Pizza(self):
        return PizzaChocolate()

    def DietPizza(self):
        return DietPizzaChocolate()

class Pizza(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ingredientes(self):
        pass

class PizzaMargherita(Pizza):
    def ingredientes(self):
        print("Queijo")

class PizzaChocolate(Pizza):
    def ingredientes(self):
        print("Chocolate")

class DietPizza(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def ingredientes(self):
        pass

class DietPizzaMargherita(DietPizza):
    def ingredientes(self):
        print("Queijo Diet")

class DietPizzaChocolate(DietPizza):
    def ingredientes(self):
        print("Chocolate Diet")

def main():
    for pizza in (Margherita(), Chocolate()):
        product_a = pizza.Pizza()
        product_b = pizza.DietPizza()
        product_a.ingredientes()
        product_b.ingredientes()

if __name__ == "__main__":
    main()