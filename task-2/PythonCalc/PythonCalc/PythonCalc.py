
import math


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
    if action != "sin" and action != "cos" and action != "tg" and action != "ctg" and action != "asin" and action != "acos" and action != "atg" and action != "actg" and action != "sqrt" and action != "bin" and action != "log" and action != "ln" and action != "%":
        for i in range(exp.count(action)):
            exp = myReplace(exp ,exp[exp.index(action) - 1 : exp.index(action) + 2], [str(eval(str(exp[exp.index(action) - 1]) + action + str(exp[exp.index(action) + 1])))])
    else:
        for i in range(exp.count(action)):
            if action == "sqrt":
                try:
                    exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.sqrt(float(exp[exp.index(action) + 1])))])
                except ValueError as ex:
                    exp = ['Error: less then zero root']
            if action == "%":
                exp = myReplace(exp ,exp[exp.index(action) - 1: exp.index(action) + 2], [str(int(float(exp[exp.index(action) - 1]) / float(exp[exp.index(action) + 1]) * 100)) + "%"])
            if action == "log":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.log(float(exp[exp.index(action) + 1]), 10))])
            if action == "ln":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.log(float(exp[exp.index(action) + 1])))])
            if action == "bin":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(bin(int(exp[exp.index(action) + 1]))).replace('0b', '')])
            if action == "sin":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.sin(float(exp[exp.index(action) + 1])))])
            if action == "cos":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.cos(float(exp[exp.index(action) + 1])))])
            if action == "tg":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.tan(float(exp[exp.index(action) + 1])))])
            if action == "ctg":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(1/math.tan(float(exp[exp.index(action) + 1])))])
            if action == "asin":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.asin(float(exp[exp.index(action) + 1])))])
            if action == "acos":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.acos(float(exp[exp.index(action) + 1])))])
            if action == "atg":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(math.atan(float(exp[exp.index(action) + 1])))])
            if action == "actg":
                exp = myReplace(exp ,exp[exp.index(action): exp.index(action) + 2], [str(1/math.atan(float(exp[exp.index(action) + 1])))])
    
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
            exp = replaceWithCalc(exp, "log")
            exp = replaceWithCalc(exp, "ln")
            exp = replaceWithCalc(exp, "bin")
            exp = replaceWithCalc(exp, "sqrt")
            exp = replaceWithCalc(exp, "asin")
            exp = replaceWithCalc(exp, "acos")
            exp = replaceWithCalc(exp, "atg")
            exp = replaceWithCalc(exp, "actg")
            exp = replaceWithCalc(exp, "sin")
            exp = replaceWithCalc(exp, "cos")
            exp = replaceWithCalc(exp, "tg")
            exp = replaceWithCalc(exp, "ctg")
            exp = replaceWithCalc(exp, "%")
            exp = replaceWithCalc(exp, "**")
            exp = replaceWithCalc(exp, "/")
            exp = replaceWithCalc(exp, "*")
            exp = replaceWithCalc(exp, "-")
            exp = replaceWithCalc(exp, "+")

            print("return:", exp)
            return exp

expression = ['5', '%', '20']
#print(replaceWithCalc(expression, "cos"))

#print(myReplace(expression, ['(', '5', '*', '(', '3', '**', '2', ')', ')'], ['45']))

print(calc(expression))