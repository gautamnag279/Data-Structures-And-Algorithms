class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums) , key = nums.count)
    
#Initially I wrote this but it exceeded the time limit
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        for i in num:
            if nums.count(i) > len(nums)//2:
                ans = i
        return ans
