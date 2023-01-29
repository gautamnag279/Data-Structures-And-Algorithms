import itertools
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(itertools.accumulate(gain, initial = 0))
