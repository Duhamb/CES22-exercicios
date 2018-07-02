# EXEMPLO PONTE #

class AbstractInterface:
	def someFunctionality(self):
		raise NotImplemented()

class Bridge(AbstractInterface):
	def __init__(self):
		self.__implementation = None

class UseCase1(Bridge):
	def __init__(self, implementation):
		self.__implementation = implementation

	def someFunctionality(self):
		print("UseCase1: ")
		self.__implementation.anotherFunctionality()

class UseCase2(Bridge):
	def __init__(self, implementation):
		self.__implementation = implementation

	def someFunctionality(self):
		print ("UseCase2: ")
		self.__implementation.anotherFunctionality()

class ImplementationInterface:
	def anotherFunctionality(self):
		raise NotImplemented

class Linux(ImplementationInterface):
	def anotherFunctionality(self):
		print("Linux!")

class Windows(ImplementationInterface):
	def anotherFunctionality(self):
		print("Windows.")

def main():
	linux = Linux()
	windows = Windows()

	# Couple of variants under a couple
	# of operating systems.
	useCase = UseCase1(linux)
	useCase.someFunctionality()

	useCase = UseCase1(windows)
	useCase.someFunctionality()

	useCase = UseCase2(linux)
	useCase.someFunctionality()

	useCase = UseCase2(windows)
	useCase.someFunctionality()

if __name__ == "__main__":
	main()