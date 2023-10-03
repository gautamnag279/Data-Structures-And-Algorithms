class Solution:
    def colName (self, n):
        ans = ''
        while n:
            remainder = (n-1)%26
            ans = chr(65 + remainder) + ans
            n = (n-1)//26
        return ans