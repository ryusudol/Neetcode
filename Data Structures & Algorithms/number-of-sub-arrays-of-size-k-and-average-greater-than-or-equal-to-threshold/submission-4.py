class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_avg = sum(arr[:k]) / k
        res = 1 if cur_avg >= threshold else 0

        for i in range(k, len(arr)):
            cur_avg += (arr[i] - arr[i - k]) / k
            if cur_avg >= threshold: res += 1
        
        return res