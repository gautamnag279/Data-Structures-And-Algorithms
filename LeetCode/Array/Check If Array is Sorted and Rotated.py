class Solution:
    def check(self, nums: List[int]) -> bool:
        sortedArray = sorted(nums)
        
        for i in range(len(nums)):
            if nums == (sortedArray[i:] + sortedArray[:i]):
                return True
            else:
                continue
        return False
            
