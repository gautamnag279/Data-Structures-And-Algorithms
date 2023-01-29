#!/bin/python3

import math
import os
import random
import re
import sys

def equalizeArray(arr):
    return len(arr) - max(arr.count(i) for i in arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
