class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        b = ["True" for i in range(0, 32) if 4**i == n]
        return False if len(b) == 0 else True
