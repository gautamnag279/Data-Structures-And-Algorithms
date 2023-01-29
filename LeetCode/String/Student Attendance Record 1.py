class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') <= 1 and s.count('LLL') == 0 :
            return True
        else:
            False
