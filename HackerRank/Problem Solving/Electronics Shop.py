import os
import sys

def getMoneySpent(keyboards, drives, b):
    lst = []
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                lst.append(i+j)
    if not in lst:
        return '-1'
    else:
        return (max(lst))
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))
    
    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
