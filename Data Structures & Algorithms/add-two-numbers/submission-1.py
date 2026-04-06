# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev, res = dummy, 0
        while l1 and l2:
            val = l1.val + l2.val + res
            prev.next = ListNode(val % 10)
            prev = prev.next
            l1, l2 = l1.next, l2.next
            res = 1 if val > 9 else 0
        while l1:
            val = l1.val + res
            prev.next = ListNode(val % 10)
            prev = prev.next
            l1 = l1.next
            res = 1 if val > 9 else 0
        while l2:
            val = l2.val + res
            prev.next = ListNode(val % 10)
            prev = prev.next
            l2 = l2.next
            res = 1 if val > 9 else 0
        if res:
            prev.next = ListNode(res)
        return dummy.next