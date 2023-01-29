class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n//5
            count += n  #count must be incremented by 'n' and not by '1'
        return count
      
'''https://leetcode.com/problems/factorial-trailing-zeroes/discuss/522315/Clear-explanation-of-the-solution-since-I-didn't-find-an-adequate-one'''
