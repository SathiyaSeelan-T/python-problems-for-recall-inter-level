def FindUncommon(s1, s2):

    # Create a dictionary.
    c = {}
    # build dictionary using first string.
    for w in s1.split(" "):
        c[w] = c.get(w, 0) + 1
    # build dictionary using second string.
    for w in s2.split(" "):
        c[w] = c.get(w, 0) + 1

    # print the results.
    for w, v in c.items():
        if v == 1:
            print(w)
    return

a = "Ramu is my friend."
b = "Somu is my boy."
FindUncommon(a, b)