#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    d1 = sum([arr[i][i] for i in range(0, n)])
    d2 = sum([arr[i][(n-1)-i] for i in range(0, n)])
    return abs(d1-d2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    
#THIS CODE IS BETTER
n = int(input())
sum = 0
for i in range(n):
    row = input().split()
    sum += int(row[i]) - int(row[-(i+1)])
print(abs(sum))
