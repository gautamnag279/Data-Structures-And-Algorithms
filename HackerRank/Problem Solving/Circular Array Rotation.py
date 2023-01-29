#I WROTE THIS CODE BUT IS PASSED 14/15 TEST CASES. Failed at TEST CASE 04

elements  , rotation , query_count = map(int , input().strip().split())
arr = list(map(int , input().strip().split()))
position = []

for i in range(0 , query_count):
    num = int(input())
    position.append(num)
    

rotated_list =  arr[-rotation:] + arr[:-rotation]

for j in position:
    print(rotated_list[j])
    
 
#SO I COPIED THIS CODE THAT ACTUALLY WORKS ON THAT TEST CASE 04
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
        new = [0 for i in range(len(a))]
        n = len(a)
        for i in range(0,n):
            if i+k <n:
                new[i+k] = a[i]
            else:
                new[(i+k)%n] = a[i]
        j = 0
        for i in queries:
            queries[j] = new[i]
            j += 1
            
        return queries
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
