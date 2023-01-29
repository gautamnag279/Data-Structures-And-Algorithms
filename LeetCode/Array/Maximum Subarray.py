class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      #float('-inf') sets the value to negetive of infinity and similarly float('inf') sets the value to positive of infinity 
        ans = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(ans, sum)
            if sum < 0:
                sum = 0
        return ans
