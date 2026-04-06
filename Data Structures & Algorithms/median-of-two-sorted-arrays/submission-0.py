class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Key: To sort elements from both arrays without using extra memory space
        A, B = nums1, nums2
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2
        if len(B) < len(A):
            A, B = B, A
        l, r = 0, len(A) - 1
        while True:
            x = (l + r) // 2
            y = half_len - (x + 1) - 1

            A_left = A[x] if x >= 0 else float("-inf")
            A_right = A[x + 1] if x + 1 < len(A) else float("inf")

            B_left = B[y] if y >= 0 else float("-inf")
            B_right = B[y + 1] if y + 1 < len(B) else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if total_len % 2:
                    return min(A_right, B_right)
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = x - 1
            else:
                l = x + 1