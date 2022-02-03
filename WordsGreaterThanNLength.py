def ExtractWords(str, n):
    b = str.split(" ")
    res = [x for x in b if len(x) > n]

    for w in res:
        print(w)
    return

a = "India is my country. I love India."
ExtractWords(a, 4)