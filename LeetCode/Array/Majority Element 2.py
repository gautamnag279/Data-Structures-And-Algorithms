class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [i for i in set(nums) if nums.count(i) > len(nums) / 3]
