from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        l = r = 0
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()
            
            if r + 1 >= k:
                ans.append(nums[queue[0]])
                l += 1
            r += 1

        return ans

        # largest = 0
        # for i in range(k):
        #     if nums[i] > nums[largest]:
        #         while queue:
        #             queue.popleft()
        #         largest = i
        #     queue.append(i)
        # r = k - 1
        # while r < len(nums):
        #     ans.append(nums[queue[0]])
        #     r += 1
        #     if nums[r] > nums[queue[0]]:
        #         while queue:
        #             queue.popleft()
        #     queue.append(r)
        # return ans