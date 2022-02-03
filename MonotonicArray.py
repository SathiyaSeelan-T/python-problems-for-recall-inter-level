def FindMonotonic(a):

    MonoType = 'Unknown'
    first = a[0]
    for i in range(1, len(a)):
        if MonoType == 'Unknown':
            if first != a[i]:
                if first < a[i]:
                    MonoType = "Ascending Monotonic"
                elif first > a[i]:
                    MonoType = "Descending Monotonic"
        else:
            if MonoType == 'Ascending Monotonic':
                if first > a[i]:
                    MonoType = 'Not Monotonic'
                    break
            else:
                if first < a[i]:
                    MonoType = 'Not Monotoic'
                    break

        first = a[i]
    return MonoType


#a = [1, 1, 1, 1, 1, 2, 3, 4, 5]
a = [5, 5, 5, 4, 3, 2, 1]
print(FindMonotonic(a))