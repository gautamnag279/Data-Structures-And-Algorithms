#Using brute force will give TIME LIMIT EXCEEDED. So instead using HashMaps is a better idea:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i,v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        return False
