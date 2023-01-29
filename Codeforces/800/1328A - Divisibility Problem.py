def maxMoves(a, b):
    if(a%b == 0):
        return 0
    else:
        return b - (a%b)

n = int(input())
for i in range(n):
    a, b = [int(i) for i in input().split(" ")]
    print(maxMoves(a, b))
    
# MY SISTER SOLVED THIS ONE 
