# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        largest = 0
        while fast and fast.next:
            if fast.val <= largest:
                return True
            largest = max(largest, fast.val)
            slow = slow.next
            fast = fast.next.next
        return False