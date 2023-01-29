from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = Counter(i.lower() for i in licensePlate if i.isalpha() == True)
        return min([j for j in words if Counter(j) & letters == letters] , key = len)
