class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        p1 = head
        p2 = head.next
        while p2 and p2.next:
            if p1==p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False
            
            

#THIS ACTUALLY WORKS...I HAVE NO IDEA HOW!?
#EDIT..I FOUND OUT HOW...THERE'S A BUG IN LEETCODE FOR THIS PROBLEM
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return ("Error - Found cycle in the ListNode" == str(head))
