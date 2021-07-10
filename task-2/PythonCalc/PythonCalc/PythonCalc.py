from tkinter import *

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
    for myi in range(len(array)):
        if array[myi] == subString:
            print("return:", myi)
            return myi
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
        print("!!!:", exp.count(action))
        print(exp)
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

def translate(exp):
    exp = str(exp).replace("√", "sqrt")
    exp = str(exp).split(' ')
    
    for i in range(len(exp)):
        if exp[i] == '-':
            exp [i] = '+'
            exp[i + 1] = "-" + exp[i + 1]
        if exp[i] == '^':
            exp[i] = '**'
        if exp[i] == 'sin' or exp[i] == 'cos' or exp[i] == 'tg' or exp[i] == 'ctg' or exp[i] == 'asin' or exp[i] == 'acos' or exp[i] == 'atg' or exp[i] == 'actg' or exp[i] == 'sqrt':
            if exp[i+1] != '(':
                exp.insert(i + 1, '(')
                exp.insert(i + 3, ')')
    return exp

def EqPressed(*event):
    if not event or event and event[0].char == '\r':
        outLb.configure(text=''.join(calc(translate(entry.get()))))

def Button1Pressed(input = ""):
    if input == "Game":
        outLb.configure(text = str(float(entry.get()) / 160) + " | " + str(float(entry.get()) % 160))
        return 0
    if input == "clear":
        entry.delete(0, END)
        return 0
    if input == "bin" and len(str(entry.get()).split(' ')) == 1 and str(entry.get())[0] != '-':
        outLb.configure(text = calc(translate('bin ( ' + str(entry.get()) + ' )')))
        return 0
    if str(input).isdigit():
        if entry.get() == "" or str(entry.get()).replace(' ' ,'')[-1].isdigit():
            entry.insert(len(str(entry.get())), str(input))
        else:
            if str(entry.get())[-1] == ' ':
                entry.insert(len(str(entry.get())), str(input))
            else:
                entry.insert(len(str(entry.get())), ' ' + str(input))
    else:
        if entry.get() == "" or str(entry.get())[-1] == ' ':
            entry.insert(len(str(entry.get())), str(input))
        else:
            entry.insert(len(str(entry.get())), ' ' + str(input))

window = Tk()
window.title("My calculator")
window.geometry('330x455')
window.bind("<Key>", EqPressed)


entry = Entry(window, width = 21, font=("Arial Bold", 20))
entry.grid(column = 0, row = 0, columnspan = 9)

outLb = Label(window, width = 20, font=("Arial Bold", 20))
outLb.grid(column = 0, row = 1, columnspan=9)

EqButto = Button(window, text="=", width = 15, font=("Arial Bold", 20), command = EqPressed)
EqButto.grid(column = 0, row = 2, columnspan=7)

ButtonClear = Button(window, text = "clear", width = 4, font=("Arial Bold", 20), command = lambda:  Button1Pressed("clear"))
ButtonClear.grid(column = 7, row = 2, columnspan=2)

numberButtonsWidth = 8
Button1 = Button(window, text = "1", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(1))
Button1.grid(column = 0, row=3, columnspan = 3)      
Button2 = Button(window, text = "2", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(2))
Button2.grid(column = 3, row=3, columnspan = 3)      
Button3 = Button(window, text = "3", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(3))
Button3.grid(column = 6, row=3, columnspan = 3)      
Button4 = Button(window, text = "4", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(4))
Button4.grid(column = 0, row=4, columnspan = 3)      
Button5 = Button(window, text = "5", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(5))
Button5.grid(column = 3, row=4, columnspan = 3)      
Button6 = Button(window, text = "6", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(6))
Button6.grid(column = 6, row=4, columnspan = 3)      
Button7 = Button(window, text = "7", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(7))
Button7.grid(column = 0, row=5, columnspan = 3)      
Button8 = Button(window, text = "8", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(8))
Button8.grid(column = 3, row=5, columnspan = 3)      
Button9 = Button(window, text = "9", width = numberButtonsWidth, font=("Arial Bold", 16), command = lambda:  Button1Pressed(9))
Button9.grid(column = 6, row=5, columnspan = 3)      
Button0 = Button(window, text = "0", width = 21, font=("Arial Bold", 16), command = lambda:  Button1Pressed(0))
Button0.grid(column = 1, row=6, columnspan = 7)

ButtonBrecket1 = Button(window, text = "(", width = 2, font=("Arial Bold", 16), command = lambda:  Button1Pressed("("))
ButtonBrecket1.grid(column = 0, row=6, columnspan = 1)
ButtonBrecket2 = Button(window, text = ")", width = 2, font=("Arial Bold", 16), command = lambda:  Button1Pressed(")"))
ButtonBrecket2.grid(column = 8, row=6, columnspan = 1)


ButtonSin = Button(window, text = "sin", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("sin"))
ButtonSin.grid(column = 0, row=7)
ButtonCos = Button(window, text = "cos", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("cos"))
ButtonCos.grid(column = 1, row=7)
ButtonTg = Button(window, text = "tg", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("tg"))
ButtonTg.grid(column = 2, row=7)
ButtonCtg = Button(window, text = "ctg", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("ctg"))
ButtonCtg.grid(column = 3, row=7)
ButtonAsin = Button(window, text = "asin", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("asin"))
ButtonAsin.grid(column = 4, row=7)
ButtonAcos = Button(window, text = "acos", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("acos"))
ButtonAcos.grid(column = 5, row=7)
ButtonAtg = Button(window, text = "atg", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("atg"))
ButtonAtg.grid(column = 6, row=7)
ButtonActg = Button(window, text = "actg", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("actg"))
ButtonActg.grid(column = 7, row=7)
ButtonActg = Button(window, text = "bin", width = 3, font=("Arial Bold", 11), command = lambda:  Button1Pressed("bin"))
ButtonActg.grid(column = 8, row=7)

ButtonPlus= Button(window, text = "+", width = 7, font=("Arial Bold", 11), command = lambda:  Button1Pressed("+"))
ButtonPlus.grid(column = 0, row=8, columnspan = 2)
ButtonSub= Button(window, text = "-", width = 7, font=("Arial Bold", 11), command = lambda:  Button1Pressed("-"))
ButtonSub.grid(column = 2, row=8, columnspan = 2)
ButtonMul= Button(window, text = "*", width = 7, font=("Arial Bold", 11), command = lambda:  Button1Pressed("*"))
ButtonMul.grid(column = 4, row=8, columnspan = 2)
ButtonDiv= Button(window, text = "/", width = 7, font=("Arial Bold", 11), command = lambda:  Button1Pressed("/"))
ButtonDiv.grid(column = 0, row=9, columnspan = 2)
ButtonDublMul= Button(window, text = "^", width = 7, font=("Arial Bold", 11), command = lambda:  Button1Pressed("^"))
ButtonDublMul.grid(column = 2, row=9, columnspan = 2)
ButtonPerc= Button(window, text = "%", width = 7, font=("Arial Bold", 11), command = lambda:  Button1Pressed("%"))
ButtonPerc.grid(column = 4, row=9, columnspan = 2)
ButtonPerc= Button(window, text = "log", width = 11, font=("Arial Bold", 11), command = lambda:  Button1Pressed("log"))
ButtonPerc.grid(column = 6, row=8, columnspan = 3)
ButtonPerc= Button(window, text = "ln", width = 11, font=("Arial Bold", 11), command = lambda:  Button1Pressed("ln"))
ButtonPerc.grid(column = 6, row=9, columnspan = 3)

ButtonSqrt= Button(window, text = "√", width = 35, font=("Arial Bold", 11), command = lambda:  Button1Pressed("√"))
ButtonSqrt.grid(column = 0, row=10, columnspan = 9)
ButtonMasha= Button(window, text = "Button for game", width = 29, font=("Arial Bold", 14), command = lambda:  Button1Pressed("Game"))
ButtonMasha.grid(column = 0, row=11, columnspan = 9)

window.mainloop()