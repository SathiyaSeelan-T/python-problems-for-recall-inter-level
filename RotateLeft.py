def RotateLeft(a, n):
    return a[n:] + a[0:n]

myarr = [5, 10, 20, 40, 70, 1, 2, 3]

print("Original array:", myarr)
print("Rotated Array :", RotateLeft(myarr, 3))