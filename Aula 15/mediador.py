# EXEMPLO MEDIADOR #

class Mediator:
	def __init__(self):
		self.Car = Car(self)
		self.Motorcycle = Motorcycle(self)
		self.Bike = Bike(self)

class Car:
	def __init__(self, mediator):
		self.mediator = mediator

class Motorcycle:
	def __init__(self, mediator):
		self.mediator = mediator

class Bike:
	def __init__(self, mediator):
		self.mediator = mediator

def main()
	mediator = Mediator()

if __name__ == "__main__":
	main()