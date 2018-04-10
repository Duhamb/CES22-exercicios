def extract_words(word):
    extract = [""]
    add = [""]
    clean_list = "abcdefghijklmnopqrstuvwxyz"
    tam = len(word)
    ref = 0
    vazio = True
    for i in range(0, tam):
        if word[i] in clean_list:
            extract[ref] += word[i]
            vazio = False
        elif not vazio and i < tam-1:
            extract += add
            ref += 1
            vazio = True
    return extract

arqEntrada = open("livro.txt")
arqSaida = open("alice_words.txt", "w")

content = arqEntrada.read().lower()
arqEntrada.close()

words = extract_words(content)

tam = len(words)

words.sort()

arqSaida.write("Word              Count\n=======================\n")

count = 0
for i in range(tam-1):
    if words[i] == words[i+1]:
        count += 1
    elif words[i] != '':
        arqSaida.write('{:<18}{}'.format(words[i], str(count))+"\n")
        count = 1