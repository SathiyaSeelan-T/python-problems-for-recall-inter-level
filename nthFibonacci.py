def NthFiboLooping(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            # print(i, c)
        return c

def NthFiboRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return NthFiboRecursive(n-1) + NthFiboRecursive(n-2)


print("Nth Fibonacci finding:")
print("======================")
print()
n = int(input("Please enter a N value: "))
print(n, "th Fibonacci term is ", NthFiboRecursive(n))
