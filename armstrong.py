# Write function to find the number of digits.
def getDigitsCount(n):
    t = n
    l = 0
    while(t > 0):
        l = l + 1
        t = t // 10     # Drop the last digit

    return l

def getArmstrong(n):
    l = getDigitsCount(n)
    s = 0
    t = n
    while(t>0):
        s = s + pow(t % 10, l)
        t = t // 10
    return s

n = int(input("Enter a number: "))
#print("No. of digits in ", n, " is ", getDigitsCount(n))
armst = getArmstrong(n)
#print("Armstrong of ", n, " is ", armst)

if(n==armst):
    print(n, " is an armstrong number.")
else:
    print(n, " is not an armstrong number.")

