class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = [str(i) for i in s.split()]
        if [arr.index(i) for i in arr] == [pattern.index(i) for i in pattern]:
            return True
        else:
            return False
