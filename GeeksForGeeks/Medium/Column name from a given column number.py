class Solution:
    def colName (self, n):
        ans = ''
        while n:
            alphabet_to_add = (n-1)%26
            ans = chr(65 + alphabet_to_add) + ans
            n = (n-1)//26
        return ans