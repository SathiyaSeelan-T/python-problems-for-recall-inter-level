def IsPalindrom(whichstr):
    revstr = whichstr[::-1]

    return whichstr == revstr

a = "ramu is my friend"

print(a, " is Palindrom ", IsPalindrom(a))