# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
    
        while cur != None: #Finding length of list
            length += 1
            cur = cur.next
        if length == 1:
            return None
        nth = length - n
        cur = head
        prev = None
        
        if nth == 0:
            return head.next
        for i in range(nth):
            prev = cur
            cur = cur.next
        

        prev.next = cur.next


        return head
