# Pascal Triangle
def DrawPascalTriangle(n):

    print("Pascal's Triangle of size: %d" % n)
    print()
    res = []
    halfway = int(n/2)
    halfwayspace = 0
    if n%2 == 0:
        halfway-=1
        halfwayspace = 1
    # No. of Rows.
    for i in range(0, n):

        thisRow = []
        # No. of Digits in Each Column
        print("    " * (halfway-i), end='')


        if i < halfway:
            print("  " * (i+halfwayspace), end='')
        else:
            print("  " * (n-i-1), end='')
        for j in range(0, i+1):
            nToPrint = 1
            if not (j == 0 or j== i):
                nToPrint = res[i-1][j-1] + res[i-1][j]
            thisRow.append(nToPrint)
            print("%4d" % (nToPrint), end='')

        res.append(thisRow)
        print()


pascalSize = int(input("Enter the Triangle Size (1-13): "))
#pascalSize = 10
DrawPascalTriangle(pascalSize)
