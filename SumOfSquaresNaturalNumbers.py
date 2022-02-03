import math
def GetSumOfSquares(N):

    sum = 0
    for i in range(1, N+1):
        sum = sum + i * i

    return sum

print("Finding Sum of Squares of First N natural numbers.")
print("==================================================")
print()
n = int(input("Enter N value: "))

print('Sum of squares of first', n, 'natural numbers is', GetSumOfSquares(n))