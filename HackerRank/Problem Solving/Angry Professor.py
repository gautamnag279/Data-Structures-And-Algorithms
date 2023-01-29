import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    count=0
    for i in a:
        if(i<=0):
            count+=1
        else:
            continue
    if (count>=k):
        answer = 'NO'
    else:
        answer = 'YES'

    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
