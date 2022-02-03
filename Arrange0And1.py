def Arrange0And1(x):
    return [m for m in x if m == 0] + [m for m in x if m == 1]

a = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]

print(Arrange0And1(a))
