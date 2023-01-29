class Solution:
    def reverse(self, x: int) -> int:
        numstr = str(abs(x))
        result = numstr[::-1]
        
        if x<0: 
            result = "-" + result
        if abs(int(result))< 2**31:
            return int(result)
        else:
            return 0
