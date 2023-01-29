#This was giving time limit exceeded
class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = [s.index(i) for i in s if s.count(i) == 1]
        if len(lst) > 0:
            return min(lst)
        else:
            return -1
            
#SO INSTEAD
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
