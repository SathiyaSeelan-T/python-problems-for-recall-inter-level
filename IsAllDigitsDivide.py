def IsAllDigitsDivide(n):
    temp = n
    while temp > 0:

        ld = temp % 10
        if ld == 0:
            temp = temp // 10
            continue

        if n % ld > 0:
            return False
        temp = temp // 10

    return True

a = 1208
if IsAllDigitsDivide(a):
    print("All digits divides it.")
else:
    print("All digits not divides it.")