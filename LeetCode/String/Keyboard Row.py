class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}
        
        ans = []
        
        for i in words:
            word = set(i.lower())
            
            if (word&set1 == word) or (word&set2 == word) or (word&set3 == word):
                ans.append(i)
        return ans
    
    #Here's an explanation in the difference between AND / &
    https://stackoverflow.com/questions/22646463/and-boolean-vs-bitwise-why-difference-in-behavior-with-lists-vs-nump
