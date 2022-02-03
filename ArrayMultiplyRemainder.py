def FindRemainder(a, n):
    first = a[0] % n
    for i in range(1, len(a)):
        first = ((first % n) * (a[i] % n)) % n

    return first

a = [12345, 839784, 349893, 4837, 398454]

print("Remainder: ", FindRemainder(a, 111))