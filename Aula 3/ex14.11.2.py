def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0) # Calc the absolute y distance
    dx = abs(x1 - x0) # CXalc the absolute x distance
    return dx == dy # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
    with any queen to its left.
    """
    for i in range(c): # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
     We’re assuming here that the_board is a permutation of column
    numbers, so we’re not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main():
    import random
    import time
    rng = random.Random() # Instantiate a generator

    bd = list(range(16)) # Generate the initial permutation
    num_found = 0
    tries = 0
    inicio = time.time()
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            tempo = time.time()-inicio
            print("Found solution {0} in {1} tries in {2} seconds.".format(bd, tries, int(tempo)))
            tries = 0
            num_found += 1

main()

# Found solution [12, 5, 0, 11, 7, 4, 2, 14, 9, 15, 3, 8, 6, 13, 1, 10] in 1150366 tries in 54 seconds.
# Found solution [10, 13, 2, 9, 3, 14, 7, 11, 1, 6, 15, 0, 4, 8, 12, 5] in 209062 tries in 59 seconds.
# Found solution [8, 10, 14, 6, 9, 0, 13, 5, 2, 15, 7, 12, 3, 1, 4, 11] in 1687755 tries in 103 seconds.
# Found solution [8, 3, 7, 13, 10, 1, 6, 14, 11, 4, 0, 9, 5, 2, 15, 12] in 2986160 tries in 207 seconds.
# Found solution [12, 10, 0, 7, 5, 1, 13, 9, 14, 6, 15, 3, 11, 8, 4, 2] in 1311357 tries in 252 seconds.
# Found solution [5, 11, 2, 12, 15, 6, 1, 13, 10, 7, 4, 14, 9, 0, 3, 8] in 3632344 tries in 342 seconds.
# Found solution [5, 11, 9, 3, 0, 13, 1, 8, 12, 15, 4, 10, 14, 6, 2, 7] in 205027 tries in 346 seconds.
# Found solution [5, 12, 0, 9, 3, 15, 2, 14, 8, 10, 13, 4, 6, 1, 11, 7] in 411212 tries in 356 seconds.
# Found solution [12, 6, 0, 2, 7, 13, 15, 9, 5, 1, 4, 11, 8, 14, 3, 10] in 5210426 tries in 481 seconds.
# Found solution [14, 12, 9, 3, 6, 13, 1, 10, 4, 0, 15, 8, 11, 2, 7, 5] in 956171 tries in 505 seconds.
