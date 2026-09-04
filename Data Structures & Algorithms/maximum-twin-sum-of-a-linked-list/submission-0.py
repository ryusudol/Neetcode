# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        twins, pivot = [], slow
        while slow:
            twins.append(slow.val)
            slow = slow.next
        
        res = 0
        while head != pivot:
            res = max(res, head.val + twins.pop())
            head = head.next
        
        return res