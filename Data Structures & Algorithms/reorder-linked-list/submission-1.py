class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid, tail = head, head.next
        while tail and tail.next:
            mid = mid.next
            tail = tail.next.next
        prev = None
        while mid:
            tmp = mid.next
            mid.next = prev
            prev = mid
            mid = tmp
        while head and prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2