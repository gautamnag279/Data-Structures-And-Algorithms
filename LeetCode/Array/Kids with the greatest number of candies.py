class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        most = max(candies)
        return [i + extraCandies >= most for i in candies]
        
