class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = set(nums)
        if len(num) < 3:
            return max(num)
    
        num.remove(max(num))
        num.remove(max(num))
        
        return max(num)
