def FindIfBinary(str):
    bset = set(str)
    a = set("10")

    return bset == a or bset == {'0'} or bset == {'1'}

x = "111111"
if FindIfBinary(x):
    print("Yes")
else:
    print("No")