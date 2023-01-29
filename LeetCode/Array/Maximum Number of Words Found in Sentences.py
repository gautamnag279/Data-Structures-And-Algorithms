class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = len(sentences[0].split())
        for i in sentences:
            if len(i.split()) > most:
                most = len(i.split())
        return most
