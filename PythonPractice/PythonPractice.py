from random import randint

numbs = []
maxNumber = -100
maxNumberId = -1

for i in range(30):
    numbs.append(randint(-100,100))
    print(numbs[i])

    if maxNumber < numbs[i]:
        maxNumber = numbs[i]
        maxNumberId = i

print("\nMax number:", maxNumber, "\nMax number id:", maxNumberId, "\n\n")

for i in range(29):
    if numbs[i] < 0 and numbs[i+1] < 0:
        print(numbs[i], numbs[i+1], "\n")

