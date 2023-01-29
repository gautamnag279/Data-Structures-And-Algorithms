import math
import os
import random
import re
import sys

def pickingNumbers(a):
    lst = []
    for i in a:
        elem = a.count(i) + a.count(i+1)
        lst.append(elem)
    return max(lst)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
