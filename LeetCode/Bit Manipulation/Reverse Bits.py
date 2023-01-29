#THIS IS GIVING VALUE ERROR
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(str(n)[::-1] , 2)
        
#SO INSTEAD
class Solution:
    def reverseBits(self, n: int) -> int:
        return int('{0:032b}'.format(n)[::-1] , 2)
                   
https://stackoverflow.com/questions/29683207/missing-zeros-when-using-format-to-make-an-integer-to-a-binary
