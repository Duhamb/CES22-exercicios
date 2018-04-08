def find_unknowns_merge_pattern_a(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
    list of words from wds that do occur in vocab.
    """

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]: # Good, word exists in vocab
            result.append(wds[yi])
            yi += 1

        elif vocab[xi] < wds[yi]: # Move past this vocab word,
            xi += 1

        else: # Got word that is not in vocab
            yi += 1

def find_unknowns_merge_pattern_b(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
    list of words from vocab that do occur in wds.
    """

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            return result

        if yi >= len(wds):
            return result

        if wds[yi] == vocab[xi]: # Good, word exists in wds
            xi += 1

        elif wds[yi] < vocab[xi]: # Move past this wds word,
            yi += 1

        else: # Got word that is not in wds
            result.append(vocab[xi])
            xi += 1

def find_unknowns_merge_pattern_c(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
    list of words from wds that do not occur in vocab.
    """

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]: # Good, word exists in vocab
            yi += 1

        elif vocab[xi] < wds[yi]: # Move past this vocab word,
            xi += 1

        else: # Got word that is not in vocab
            result.append(wds[yi])
            yi += 1

def find_unknowns_merge_pattern_d(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
    list of words that are present in either the first or the second list.
    """

    result = []
    xi = 0
    yi = 0
    last = None

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            result.extend(vocab[xi:])
            return result

        if vocab[xi] == wds[yi]: # Good, word exists in vocab
            if vocab[xi] != last:
                result.append(vocab[xi])
                last = vocab[xi]
            xi += 1
            yi += 1

        elif vocab[xi] < wds[yi]: # Move past this vocab word,
            if vocab[xi] != last:
                result.append(vocab[xi])
                last = vocab[xi]
            xi += 1

        else: # Got word that is not in vocab
            if wds[yi] != last:
                result.append(wds[yi])
                last = wds[yi]
            yi += 1

def find_unknowns_merge_pattern_e(vocab, wds):
    """ Both the vocab and wds must be sorted. Return a new
    list of words from vocab that do occur in wds.
    """

    result = []
    reference = wds
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            return result

        if yi >= len(reference):
            return result

        if reference[yi] == vocab[xi]: # Good, word exists in wds
            reference.remove(reference[yi])
            xi += 1

        elif reference[yi] < vocab[xi]: # Move past this wds word,
            yi += 1

        else: # Got word that is not in wds
            result.append(vocab[xi])
            xi += 1

vocab = [1,2,2,3,4,5,6,7,8,9,10]
wds = [2,4,6,8,10,12]

print(find_unknowns_merge_pattern_a(vocab,wds))
print(find_unknowns_merge_pattern_b(vocab,wds))
print(find_unknowns_merge_pattern_c(vocab,wds))
print(find_unknowns_merge_pattern_d(vocab,wds))
print(find_unknowns_merge_pattern_e(vocab,wds))