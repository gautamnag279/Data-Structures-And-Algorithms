# There is a formula for this
# https://leetcode.com/problems/arranging-coins/discuss/714130/Python-Math-oneliner-explained

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(2*n + 0.25) - 0.5)
