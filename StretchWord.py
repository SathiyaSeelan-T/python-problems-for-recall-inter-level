def StretchWord(str, rl, indices):

    el = rl - len(str)
    if el < 0:
        return []
    elif el==0:
        return [].append(str)

    result = []
    for i in range(len(str)):
        for j in range(1, el+1):
            for m in range(i, len(str)):
                tres = str[:m] + str[m] * (el-j) + str[m:]
                tres2 = [x for x in tres]
                tres2.insert(i, str[i] * j)
                res = "".join(tres2)
                if res not in result:
                    result.append(res)
    result.sort()
    if indices == []:
        return result

    # filtering option comes here.
    finalresult = []
    for i in indices:
        finalresult.append(result[i])

    return finalresult

s = "JAVA"
reqlen = 6
ind = [0, 4, 6]
# ind = []
res = StretchWord(s, reqlen, ind)
print("Result of Stretched words:")
for i in res:
    print(i)
