class Solution:
    def isValid(self, s: str) -> bool:
        dict={')' : '(' , '}' : '{' , ']' : '['}
        stack = []
        for i in s:
            if i not in dict:
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != dict[i]:
                return False
        if len(stack) == 0:
            return True
