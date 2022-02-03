from random import randint
from random import seed
def PrintRandom():
    r = {}
    seed(1013)
    for i in range(0, 1000):
        rn = randint(0, 100)
        r[rn] = r.get(rn, 0) + 1

    # Display Random table.
    for k in sorted(r):
        print(k, r[k])

    return

PrintRandom()