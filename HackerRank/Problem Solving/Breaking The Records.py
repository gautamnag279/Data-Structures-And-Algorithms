#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    min_record = 0
    max_record = 0

    for i in range(1, len(scores)):
        if min > scores[i]:
            min = scores[i]
            min_record += 1
        elif max < scores[i]:
            max = scores[i]
            max_record += 1

    return  max_record, min_record
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
