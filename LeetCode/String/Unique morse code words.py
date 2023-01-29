class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = {"a": ".-", 
                 "b": "-...", 
                 "c": "-.-.", 
                 "d": "-..",
                 "e": ".", 
                 "f": "..-.", 
                 "g": "--.", 
                 "h": "....", 
                 "i": "..",
                 "j": ".---", 
                 "k": "-.-", 
                 "l": ".-..", 
                 "m": "--", 
                 "n": "-.", 
                 "o": "---", 
                 "p": ".--.", 
                 "q": "--.-",
                 "r": ".-.", 
                 "s": "...", 
                 "t": "-", 
                 "u": "..-", 
                 "v": "...-", 
                 "w": ".--", 
                 "x": "-..-", 
                 "y": "-.--", 
                 "z": "--.."}
        
        ans = set()
        
        for i in words:
            arr = []
            for j in i:
                arr.append(codes.get(j))
            ans.add("".join(arr))
            
        return len(ans)
