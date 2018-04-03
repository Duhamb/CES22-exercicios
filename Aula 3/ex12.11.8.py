import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def cleanword(word):
    clean_word =""
    tam = len(word)
    clean_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, tam):
        if word[i] in clean_list:
            clean_word += word[i]
    return clean_word

def has_dashdash(word):
    tam = len(word)
    for i in range(0, tam-1):
        if word[i] == '-' and word[i+1] == '-':
            return True
    return False

def extract_words(word):
    extract = [""]
    add = [""]
    clean_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tam = len(word)
    ref = 0
    vazio = True
    for i in range(0, tam):
        if word[i] in clean_list:
            extract[ref] += word[i].lower()
            vazio = False
        elif not vazio and i < tam-1:
            extract += add
            ref += 1
            vazio = True
    return extract

def wordcount(word, list):
    tam = len(list)
    times = 0
    for i in range(0, tam):
        if list[i] == word:
            times += 1
    return times

def wordset(lista):
    tam = len(lista)
    lista.sort()
    for i in range(tam-1, 0, -1):
        if lista[i] == lista[i-1]:
            del lista[i]
    return lista

def longestword(lista):
    max = 0
    tam = len(lista)
    for i in range(0, tam):
        if len(lista[i]) > max:
            max = len(lista[i])
    return max

test(cleanword("what?") == "what")
test(cleanword("’now!’") == "now")
test(cleanword("?+=’w-o-r-d!,@$()’") == "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time! ’Now’, is the time? Yes, now.") == ["now","is","the","time","now","is","the","time","yes","now"])
test(extract_words("she tried to curtsey as she spoke--fancy") == ["she","tried","to","curtsey","as","she","spoke","fancy"])

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)