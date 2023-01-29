class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return s[::-1]
        if len(s) > k and len(s) <= k*2:
            return s[:k][::-1] + s[k:]
        
        ans = ""
        
        for i in range(0 , len(s) , 2*k):
            ans += s[i:i+k][::-1] + s[i+k:i+2*k]
        
        return ans
    
