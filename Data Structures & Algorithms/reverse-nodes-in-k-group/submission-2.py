# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur, tail = head, head
        is_end = False

        for _ in range(k - 1):
            if not head:
                return head
            head = head.next

        prev_tail = None
        while tail:
            prev = None
            tmp_head = cur

            for _ in range(k):
                if not tail:
                    is_end = True
                    break
                tail = tail.next
            
            if is_end:
                prev_tail.next = tmp_head
                break

            while cur != tail:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            if prev_tail:
                prev_tail.next = prev
            prev_tail = tmp_head
        return head