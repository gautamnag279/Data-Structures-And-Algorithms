class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word or word.lower() == word or word.title() == word:
            return True
        else:
            return False
