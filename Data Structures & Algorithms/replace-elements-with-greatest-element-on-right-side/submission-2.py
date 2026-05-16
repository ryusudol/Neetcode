class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_seen = -1
        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            arr[i] = largest_seen
            largest_seen = max(largest_seen, cur)
        return arr