def revWords(str):
    b = str.split(" ")
    c = b[-1::-1]
    return ' '.join(c)

a = "Ramu is my friend"
print(revWords(a))