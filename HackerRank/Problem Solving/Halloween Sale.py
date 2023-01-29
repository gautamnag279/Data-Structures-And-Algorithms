#!/bin/python3

import math
import os
import random
import re
import sys

#this failed 4 test case
def howManyGames(p, d, m, s):
    arr = [i for i in range(p, m, -d)]
    diff = [i for i in range(1, s) if m*i <= s - sum(arr)]
    if len(arr) < 1:
        return s
    elif len(diff) < 1:
        return 0
    else:
        return (len(arr) + len(diff))

#so instead
def howManyGames(p, d, m, s):
    games = 0
    while s >= 0:
        s -= p
        p = max(p - d, m)
        games += 1
    return games - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
