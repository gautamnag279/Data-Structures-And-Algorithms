class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s2 = sorted(s)
        t2 = sorted(t)
        s3 = "".join(s2)
        t3 = "".join(t2)
        if s3 == t3:
            return True
        else:
            return False
        
