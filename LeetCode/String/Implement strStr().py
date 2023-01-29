class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            c = haystack.index(needle)
            return c
        except:
            return -1
