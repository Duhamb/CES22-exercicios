arqEntrada = open("entrada.txt", "r")
arqSaida = open("saida.txt", "w")

lines = arqEntrada.readlines()
lines.reverse()

arqSaida.write(lines[0] + "\n")
arqSaida.writelines(lines[1::])