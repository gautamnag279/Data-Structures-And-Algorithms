#POOR RUNTIME AND POOR MEMORY USAGE
from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(Counter(stones)[i] for i in jewels)

#GOOD EFFICIENCY AND MEDIOCRE MEMORY USAGE
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(i in jewels for i in stones)
