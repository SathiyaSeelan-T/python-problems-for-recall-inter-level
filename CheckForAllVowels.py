def Check4AllVowels(s):

    # Make all characters lowercase.
    s = s.lower()
    vowels = set("aeiou")
    fvowels = set({})

    # Check for individual characters.
    for c in s:
        if c in vowels:
            fvowels.add(c)

    if len(vowels) == len(fvowels):
        print("Accepted.")
    else:
        print("Not accepted.")
        print("Missing Vowels: " + "".join(vowels-fvowels))

a = input("Enter a sentence: ")
Check4AllVowels(a)