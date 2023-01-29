class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        b = ["True" for i in range (0, 32) if 3**i == n]
        if len(b) == 0:
            return False
        else:
            return True
