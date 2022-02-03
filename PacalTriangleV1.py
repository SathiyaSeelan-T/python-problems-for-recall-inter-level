# Pascal's triangle
def DrawPascalTriangle(n):

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

print(DrawPascalTriangle(7))