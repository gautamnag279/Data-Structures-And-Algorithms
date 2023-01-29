class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ranged_list = [i for i in range(1, len(nums) + 1)]
        return list(set(ranged_list) - set(nums))
