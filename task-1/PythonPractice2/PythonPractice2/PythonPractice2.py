# 1. start
string = str(input("\nWrite yout string:\n"))
# 1. end
print("\nstart string:", string)
finalString = ""
numbers = []
maxInNumbers = 0
finalNumbers = []

# 2. start
flag = False
for letter in string:
    if letter.isdigit():
        if flag:
            numbers[len(numbers) - 1] += str(letter)
        else:
            numbers.append(letter)
        flag = True
    else:
        flag = False
# 2. end

# 3. start
numbers = [int(x) for x in numbers]
# 3. end

# 4. start
string = string.replace('0', '')
string = string.replace('1', '')
string = string.replace('2', '')
string = string.replace('3', '')
string = string.replace('4', '')
string = string.replace('5', '')
string = string.replace('6', '')
string = string.replace('7', '')
string = string.replace('8', '')
string = string.replace('9', '')
# 4. end

print("removed numbers:", string, numbers)

# 5. start
dividedString = string.split(' ')
# 5. end

# 6. start
for word in dividedString:
    if word:
        word = str(word).upper()[0] + word[1:]
        word = word[:len(word) - 1] + str(word).upper()[len(word) - 1]
        finalString += word + ' '
# 6. end

print()
print("final string:", finalString)

# 7. start
if numbers != []:
    maxInNumbers = max(numbers)
    print("\nMax number is", maxInNumbers)
else:
    print("There is not numbers :/")
# 7. end

# 8. start
for i in range(len(numbers)):
    if numbers[i] != maxInNumbers:
        finalNumbers.append(int(numbers[i]) ** i)
    else:
        finalNumbers.append(numbers[i])
# 8. end

print("final numbers array:", finalNumbers)
print("\n\n")