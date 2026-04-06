class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        target = intervals[0]
        for i in range(1, len(intervals)):
            if target[1] < intervals[i][0]:
                ans.append(target)
                target = intervals[i]
            elif target[0] > intervals[i][1]:
                ans.appned(intervals[i])
            else:
                target = [
                    min(target[0], intervals[i][0]),
                    max(target[1], intervals[i][1]),
                ]
        ans.append(target)
        return ans