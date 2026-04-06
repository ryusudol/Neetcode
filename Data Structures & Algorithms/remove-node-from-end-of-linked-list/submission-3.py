# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        while n:
            right = right.next
            n -= 1
        while right:
            left, right = left.next, right.next
        left.next = left.next.next
        return dummy.next
        # sz = 0
        # cur = head
        # while cur:
        #     sz += 1
        #     cur = cur.next
        # n = sz - n
        # cur, prev = head, None
        # while n:
        #     prev = cur
        #     cur = cur.next
        #     n -= 1
        # if prev:
        #     prev.next = cur.next
        # else:
        #     head = head.next
        # return head