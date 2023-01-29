class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0" #using the quotation is necessary as the result is expected as a string
        elif num < 0:
            num += 2**32
            
        stack = []
        s = "0123456789abcdef"
        
        while num != 0:
            stack.append(s[num%16])
            num //= 16
        
        stack.reverse()
        return "".join(stack)
            
            
