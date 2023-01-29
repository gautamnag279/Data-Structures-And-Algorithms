class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = int(''.join([str(i) for i in digits]))+1
        return [int(j) for j in str(value)]
