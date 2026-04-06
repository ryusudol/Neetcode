class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = l = total = 0
        for r in range(len(arr)):
            if r - l + 1 > k:
                total -= arr[l]
                l += 1
            total += arr[r]
            if r - l + 1 == k:
                ans += 1 if total / k >= threshold else 0
        return ans