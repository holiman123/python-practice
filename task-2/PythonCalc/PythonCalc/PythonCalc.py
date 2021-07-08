
def myReplace(array, replaced, replacing):
    print("my raplace:", ''.join(array) ,''.join(replaced), ''.join(replacing))
    flag = False
    index = -1
    finalArray = list(array)

    for i in range(len(array) - len(replaced) + 1):
        flag = True
        for j in range(len(replaced)):
            if array[i + j] != replaced[j]:
                flag = False
        if flag:
            index = i

    for i in range(len(replaced)):
        del finalArray[index]

    for i in range(len(replacing)):
        finalArray.insert(index + i, replacing[i])

    print("final:", ''.join(finalArray))
    return finalArray

def myLIndex(array, subString):
    print("find left index in:", ''.join(array), ''.join(subString))
    for i in range(len(array)):
        if array[i] == subString:
            print("return:", i)
            return i
    print("return:", i)
    return -1

def myRIndex(array, subString):
    print("find right index in:", ''.join(array), ''.join(subString))
    outIndex = -1
    for i in range(len(array)):
        if array[i] == subString:
            outIndex = i
    print("return:", outIndex)
    return outIndex

def replaceWithCalc(exp, action):
    print("replace with calc:", ''.join(exp), action)
    for i in range(exp.count(action)):
        exp = myReplace(exp ,exp[exp.index(action) - 1 : exp.index(action) + 2], [str(eval(str(exp[exp.index(action) - 1]) + action + str(exp[exp.index(action) + 1])))])
    print("return:", ''.join(exp))
    return exp

def calc(exp):
    print("calc", ''.join(exp))
    while(True):
        if myLIndex(exp, "(") != -1:
            i = myLIndex(exp, "(") + 1
            bracketCount = 1
            while(True):
                if(exp[i] == "("):
                    bracketCount += 1
                if(exp[i] == ")"):
                    bracketCount -= 1
                if(bracketCount == 0):
                    exp = myReplace(exp, exp[myLIndex(exp, "("):i + 1], calc(exp[myLIndex(exp, "(") + 1: i + 0]))
                    break
                i += 1
        else:
            exp = replaceWithCalc(exp, "**")
            exp = replaceWithCalc(exp, "/")
            exp = replaceWithCalc(exp, "*")
            exp = replaceWithCalc(exp, "-")
            exp = replaceWithCalc(exp, "+")

            print("return:", exp)
            return exp

expression = ['1', '+', '(', '5', '*', '(', '3', '**', '2', ')', ')', '-', '4', '+', '(', '1', '+', '1', ')']

#print(myReplace(expression, ['(', '5', '*', '(', '3', '**', '2', ')', ')'], ['45']))

print(calc(expression))