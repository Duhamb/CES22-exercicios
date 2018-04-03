import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def reverse(word):
    tam = len(word)
    rev_word = ""
    for i in range(0, tam):
        rev_word = word[i] + rev_word
    return rev_word

def is_palindrome(word):
    rev_word = reverse(word)
    if rev_word == word:
        return True
    else:
        return False

test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))