# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        while l1 != None or l2 != None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            numSum = cur.val + val1 + val2
            if numSum >= 10:
                cur.val = numSum - 10
                cur.next = ListNode(1)
            else:
                cur.val = numSum
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 != None or l2 != None:
                if cur.next == None:
                    cur.next = ListNode()
                cur = cur.next

        return res
        



