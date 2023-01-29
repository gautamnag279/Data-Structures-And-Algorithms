#THE CODE WORKS JUST FINE, BYT THE MEMORY EFFICIENCY SUCKS!
class Solution:
    def reverseWords(self, s: str) -> str:
        lst = list(s.split())
        arr = [i[::-1] for i in lst]
        return " ".join(arr)
        
#SO INSTEAD
class Solution:
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])[::-1]
