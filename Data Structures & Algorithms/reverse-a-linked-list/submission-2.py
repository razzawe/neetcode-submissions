# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Make each current element point to the previous element
        prev, curr = None, head

        # 1->2->3
        # 1-> Null
        #then... prev = 1, curr = 2 (the old next before being replaced)
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp


     

        return prev


       

