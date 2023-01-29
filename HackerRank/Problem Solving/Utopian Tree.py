#!/bin/python3

import math
import os
import random
import re
import sys

def utopianTree(n):
    growth = 0
    
    for i in range(n+1):
        if i%2 ==0:
            growth = growth + 1
        else:
            growth = growth * 2
            
    return growth

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
