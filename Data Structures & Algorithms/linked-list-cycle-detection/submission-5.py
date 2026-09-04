# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        iteration = 0
        while head:
            head = head.next
            iteration += 1
            if iteration > 1000:
                return True
        return False