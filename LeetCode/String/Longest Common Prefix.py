class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not(strs):
            return ""
        pref = ""
        for i in zip(*strs):
            if len(set(i)) != 1:
                return pref
            pref += i[0]
            
        return pref
        
#A MORE DETAILED SOLUTION
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == None:
            print("List is None")
            return("")
        
        length = len(strs)
        if length == 0:
            print("List is empty")
            return("")
        
        if length == 1:
            print("List has just 1 string")
            return(strs[0])
        
        retStr = ""
        
        firstStr = strs[0]
        
        '''
         Take the first string of the list and compare its characters with characters in other strings of the list
         Outer for loop is to iterate through the chars of the first string
         Inner for loop is tp iterate from 2nd to the last string in the list
         Time-Complexity : O(m * n), m = length of the first string, n = total no. of strings in the list
         Space-Complexity : O(1), no extra space except two strings, retStr and firstStr.
        '''
        
        for i in range(len(firstStr)):
            for j in range(1, length):
                if i < len(strs[j]):
                    if firstStr[i] != strs[j][i]:
                        return(retStr)
                else:
                    return(retStr)
            retStr = retStr + firstStr[i]
        
        return(retStr)
