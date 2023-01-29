class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current = head
        previous = None
        
        while current is not None:
            if current.val == val and current == head:
                head = head.next
            elif current.val != val:
                previous = current
                else:
                    previous.next = head.next
                


#THIS IS MUCH EASIER TO UNDERSTAND
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = None
        
        while(curr):
            if curr.val == val: 
                if curr == head:
                    head = head.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next
        
        return head
