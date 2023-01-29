class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 4:
            n = sum(int(i)**2 for i in str(n))
        return n == 1
            
