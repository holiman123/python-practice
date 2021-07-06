
def myReplace(array, replaced, replacing):
    flag = False
    index = -1
    finalArray = list(array)

    for i in range(len(array) - len(replaced) + 1):
        flag = False
        for j in range(len(replaced)):
            if array[i + j] == replaced[j]:
                flag = True
        if flag:
            index = i

    for i in range(len(replaced)):
        del finalArray[index]


    for i in range(len(replacing)):
        finalArray.insert(index + i, replacing[i])

    return finalArray

def myLIndex(array, subString):
    for i in range(len(array)):
        if array[i] == subString:
            return i

def myRIndex(array, subString):
    outIndex = -1
    for i in range(len(array)):
        if array[i] == subString:
            outIndex = i
    return outIndex

def calc(exp):

    for k in range(2):
        if myLIndex(exp, "(") != -1 and myRIndex(exp, ")") != -1:
            exp = myReplace(exp, exp[myLIndex(exp, "("):myRIndex(exp, ")") + 1], calc(exp[myLIndex(exp, "(") + 1: myRIndex(exp, ")") + 0]))
        else:
           for i in range(exp.count("*")):
               exp = myReplace(exp ,exp[exp.index("*") - 1 : exp.index("*") + 2], [str(float(exp[exp.index("*") - 1]) * float(exp[exp.index("*") + 1]))])



    return exp

expression = ['1', '+', '(', '5', '*', '6', ')', '*', '4']

#print(myReplace(expression, ['475.0', '*', '4'], ['1900']))

print(calc(expression))