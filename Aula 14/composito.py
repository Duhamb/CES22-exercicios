# EXEMPLO COMPÓSITO #

class Component(object):
	def __init__(self, *args, **kw):
		pass

	def component_function(self):
		pass

class Topico(Component):
	def __init__(self, name, *args, **kw):
		Component.__init__(self, *args, **kw)
		self.name = name

	def component_function(self):
		print("\t" + self.name)

class Capitulo(Component):
	def __init__(self, name, *args, **kw):
		Component.__init__(self, *args, **kw)
		self.name = name
		self.children = []

	def append_child(self, child):
		self.children.append(child)

	def remove_child(self, child):
		self.children.remove(child)

	def component_function(self):
		print(self.name)
		list(map(lambda x: x.component_function(), self.children))

def main()
	ConjNum = Capitulo("Conjuntos Numéricos")
	NumNaturais = Topico("NumerosNaturais")
	NumInteiros = Topico("NumerosInteiros")
	NumRacionais = Topico("NumerosRacionais")
	NumIrracionais = Topico("NumerosIrracionais")
	NumReais = Topico("NumerosReais")
	ConjNum.append_child(NumNaturais)
	ConjNum.append_child(NumInteiros)
	ConjNum.append_child(NumRacionais)
	ConjNum.append_child(NumIrracionais)
	ConjNum.append_child(NumReais)
	Livro = Capitulo("Matemática Elementar")
	Livro.append_child(ConjNum)
	Livro.component_function()

if __name__ == "__main__":
	main()