class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1
        
        while leftPointer < rightPointer:
            if s[leftPointer] != s[rightPointer]:
                str1 = s[leftPointer:rightPointer]
                str2 = s[leftPointer + 1 : rightPointer + 1]
                return str1 == str1[::-1] or str2 == str2[::-1]
            
            leftPointer += 1
            rightPointer -= 1
        
        return True
            
