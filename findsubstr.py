def FindWord(mainstr, findstr):
    b = mainstr.lower().split(" ")
    if findstr.lower() in b:
        return "Yes, found the word."
    else:
        return "No, not found."

a = input("Enter a sentence: ")
b = input("Enter the word to find: ")
print(FindWord(a, b))
