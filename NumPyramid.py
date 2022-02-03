def PrintNumPyramid(n):

    # Control the overall lines.
    for i in range(1, n+1):
        # Print spaces before Pyramid
        print(" " * (n-i), end='')
        for j in range(1, i+1):
            print("%1d" % j, end='')

        # print the second half.
        for j in range(i-1, 0, -1):
            print("%1d" % j, end='')

        print()


PrintNumPyramid(7)