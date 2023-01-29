#THIS WAS ONLY FASTER THAN 5% OF THE SOLUTIONS
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = int(a , 2) + int(b , 2)
        return bin(add)[2:]

#BUT IF I DO THIS, IT MAKES IT FASTER THAN 97% OF THE SOLUTIONS...LIKE WTF!
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = int(a, 2) + int(b, 2)
        return bin(add).replace("0b", "")

