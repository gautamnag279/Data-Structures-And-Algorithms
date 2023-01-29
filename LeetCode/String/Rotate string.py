class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in (s+s) and len(goal) == len(s)
