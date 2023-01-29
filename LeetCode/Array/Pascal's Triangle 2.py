import math

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        
        for i in range(0, 34):
            temp = []
            for j in range(0,i+1):
                nCr = math.comb(i, j)
                temp.append(nCr)
            ans.append(temp)
        
        return(ans[rowIndex])
