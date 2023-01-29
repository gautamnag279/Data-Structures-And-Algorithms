import math

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for i in range(0, numRows):
            temp = []
            for j in range(0, i+1):
                nCr = math.comb(i,j)
                temp.append(nCr)
            ans.append(temp)
            
        return ans

#This is how the code works for n = 5 in the forr loops:

i j nCr
0 0 1
1 0 1
1 1 1
2 0 1
2 1 2
2 2 1
3 0 1
3 1 3
3 2 3
3 3 1
4 0 1
4 1 4
4 2 6
4 3 4
4 4 1
