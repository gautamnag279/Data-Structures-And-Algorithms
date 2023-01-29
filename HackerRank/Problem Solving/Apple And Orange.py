#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount = 0
    orangeCount = 0
    for i in range(len(apples)):
        temp = a + apples[i]
        if(temp in range(s , t+1)):
            appleCount +=1
    for j in range(len(oranges)):
        temp = b + oranges[j]
        if(temp in range(s , t+1)):
            orangeCount +=1
    print(appleCount)
    print(orangeCount)
        
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
