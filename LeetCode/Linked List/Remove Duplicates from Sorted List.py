# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:                                # First, check if the list is empty or not
            return None                             # If YES, then return None
        
        tracker = head                              # Else, take tracker variable pointing at the 'head' node
        
        while tracker.next:                         # Traverse till the next node is not None
            if tracker.val == tracker.next.val:     # Check if the current node's value and the next node's values are same or not
                tracker.next = tracker.next.next    # If YES, then change the next node's pointer to next node's next pointer
                continue                            # And continue to the top
                
            tracker = tracker.next                  # Else, Move the tracker to the next node  
            if not tracker:                         # Check if tracker reached to the last node or not
                break                               # If YES, then break the loop
                
        return head                                 # Finally, return 'head' with all the duplicates removed from the list

    
    
    
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tracker = head
        
        while tracker:
            if tracker.next != None and tracker.val == tracker.next.val:
                tracker.next = tracker.next.next
            else:
                tracker = tracker.next
        return head 
