#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positiveCount = 0
    negetiveCount = 0
    neutralCount = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            positiveCount += 1
        if arr[i] == 0:
            neutralCount += 1
        if arr[i] < 0:
            negetiveCount += 1
    print(positiveCount/len(arr))
    print(negetiveCount/len(arr))
    print(neutralCount/len(arr))
            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
