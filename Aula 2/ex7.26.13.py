list_is_eulerian = {1, 2, 5, 6} # Found by inspection

for i in range(1, 6):
    if i in list_is_eulerian:
        print("Drawn number {0} is an Eulerian trail".format(i))
    else:
        print("Drawn number {0} isn't an Eulerian trail".format(i))