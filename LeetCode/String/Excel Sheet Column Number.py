class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in s:
            result = (result *26 + ord(i)-65) + 1
        return result
