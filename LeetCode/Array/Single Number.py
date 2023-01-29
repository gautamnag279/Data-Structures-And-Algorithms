class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum = 0
        for i in nums:
            sum = sum^i
        return sum
