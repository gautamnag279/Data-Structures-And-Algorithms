class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,v in enumerate(numbers):
            diff = target - v
            if diff in hashMap:
                return [hashMap[diff]+1 , i+1]
            else:
                hashMap[v] = i
                
