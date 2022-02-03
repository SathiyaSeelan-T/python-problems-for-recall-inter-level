def FindUniqueLetters(S1, S2):
    aset = set(S1)
    bset = set(S2)

    return len(aset & bset)

a = "Ramu is my friend"
b = "Ramu found us"
print(FindUniqueLetters(a, b)," unique characters found.")