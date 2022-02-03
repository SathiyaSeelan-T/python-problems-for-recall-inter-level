# This function finds the Greatest Common Divisor value
# using Euclid's Algorithm
def gcd(a, b):
    # Repeat the subtraction process until both are equal.
    while a != b:
        # print("a=%d b=%d" % (a, b))
        if a > b:
            a = a - b
        else:
            b = b - a

    return a

# Find the LCM of a and b
def lcm(a, b):
    return (a * b) / gcd(a,b)

x = 4
y = 10
print("GCD = %d " % (gcd(x, y)) )
print("LCM = %d " % (lcm(x, y)))
