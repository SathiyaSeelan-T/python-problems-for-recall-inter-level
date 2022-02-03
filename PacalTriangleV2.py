# Pascal's triangle
def GetPascalTriangle(n):

    res = []
    # Control the number of rows.
    for i in range(1, n+1):

        rowVals = []
        # Control the column numbers.
        for j in range(1, i+1):
            elem = 1
            # In each row: first and last element must be 1.
            if j==1 or j==i:
                elem = 1
            else:
                # Identity the current row, 0 based.
                curRow = i-1
                # Calculate preRow based on curRow
                preRow = curRow - 1
                # Identify 0 based current Pos.
                curPos = j-1
                elem = res[preRow][curPos-1] + res[preRow][curPos]
            rowVals.append(elem)

        res.append(rowVals)
    return res

def DrawPascalTriangle(n):
    res = GetPascalTriangle(n)
    spcn = n-1
    for lst in res:
        print("   " * spcn, end='')
        for n in lst:
            print("{0:^6d}".format(n), end='')
        print()
        spcn -= 1


DrawPascalTriangle(14)