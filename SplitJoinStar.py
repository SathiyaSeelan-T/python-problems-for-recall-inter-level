def SplitJoinStar(str):
    b = list(reversed(str.split(" ")))
    return "*".join(b)


a = "Ramu is my friend"
print(SplitJoinStar(a))