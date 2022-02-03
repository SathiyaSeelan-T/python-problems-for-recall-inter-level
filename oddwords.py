def FindOddWords(str):
    b = str.split(" ")
    c = [x for x in b if len(x) % 2 == 1]
    for o in c:
        print(o)


a = "Seema is my friend and good teacher"
FindOddWords(a)