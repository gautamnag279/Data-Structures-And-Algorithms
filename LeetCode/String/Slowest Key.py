#This fails one testcase where the result needs to be in lexicological order.
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        haptics = [0]*len(releaseTimes)
        haptics[0] = releaseTimes[0]
        
        for i in range(1, len(releaseTimes)):
            haptics[i] = abs(releaseTimes[i] - releaseTimes[i-1])
            
        idx = haptics.index(max(haptics))
        
        return keysPressed[idx]
        
#So Mr. Stephan Pochmann comes to aid
class Solution:
    def slowestKey(self, r, k):
      return max(zip(map(sub, r, [0, *r]), k))[1]
    
