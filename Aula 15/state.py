# EXEMPLO STATE #

import abc

class Lampada:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

class State(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self):
        pass

class Ligar(State):
    def handle(self):
        print("Ligado")

class Desligar(State):
    def handle(self):
        print("Desligado")

def main():
    Ligado = Ligar()
    Desligado = Desligar()
    Lampada1 = Lampada(Ligado)
    Lampada1.request()
    Lampada1 = Lampada(Desligado)
    Lampada1.request()

if __name__ == "__main__":
    main()