import math
def IsPrime(n):
    sqrtn = int(math.sqrt(n))
    prime = True            # I assume this as a prime number.

    for divisor in range(2, sqrtn+1):
        if(n % divisor == 0):
            prime = False
            break

    return prime

print("Prime or Composite Number identification program:")
n = int(input("Enter a number :"))

if(n <2 ):
    print(n, "is neither prime not composite.")
else:
    if(IsPrime(n)):
        print(n, "is a prime number.")
    else:
        print(n, "is a composite number.")

