#I WROTE THIS BUT IT GAVE OUT ANSWERS WITH WHITESPACE BETWEEN EACH LETTER AND USING JOIN DIDN'T SEEM TO WORK
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash = {i: list1.index(i) + list2.index(i) for i in set(list1) & set(list2)}
        return [min(hash , key = hash.get)]

#SO INSTEAD
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash = {i: list1.index(i) + list2.index(i) for i in set(list1) & set(list2)}
        return [i for i in hash if hash[i] == min(hash.values())]
