word = input()
countLower = len([i for i in word if i.islower()])
countUpper = len([i for i in word if i.isupper()])

if (countLower >= countUpper):
    print(word.lower())
else:
    print(word.upper())
