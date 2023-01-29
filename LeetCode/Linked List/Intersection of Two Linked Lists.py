#SOLUTION 1 - MORE EFFECTIVE
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        h1 = headA
        h2 = headB
        
        while h1 != h2:
            h1 = headB if not h1 else h1.next
            h2 = headA if not h2 else h2.next
        return h1
#SOLUION 2 - EASIER TO UNDERSTAND
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA , curB = headA , headB
        visited = set()
        
        while curA:
            visited.add(curA)
            curA = curA.next
        while curB:
            if curB in visited:
                return curB
            curB = curB.next
        return None
